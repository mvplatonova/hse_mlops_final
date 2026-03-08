import time
import json
import os
import logging
from contextlib import asynccontextmanager

import psycopg2
from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from starlette.responses import Response

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("app")

model = None
db_conn = None

requests_total = Counter("predict_requests_total", "total requests")
request_latency = Histogram("predict_latency_seconds", "latency")


@asynccontextmanager
async def lifespan(app: FastAPI):
    global model, db_conn

    iris = load_iris()
    model = LogisticRegression(max_iter=200)
    model.fit(iris.data, iris.target)

    db_url = os.getenv("DATABASE_URL")
    if db_url:
        try:
            db_conn = psycopg2.connect(db_url)
            db_conn.autocommit = True
            db_conn.cursor().execute("""
                CREATE TABLE IF NOT EXISTS predictions (
                    id SERIAL PRIMARY KEY,
                    features TEXT,
                    prediction INT,
                    duration_ms FLOAT,
                    ts TIMESTAMP DEFAULT NOW()
                )
            """)
        except Exception as e:
            logger.warning(f"db error: {e}")

    yield


app = FastAPI(lifespan=lifespan)


class PredictRequest(BaseModel):
    features: list[float]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


@app.post("/api/v1/predict")
def predict(req: PredictRequest):
    t = time.time()
    pred = int(model.predict([req.features])[0])
    duration = time.time() - t

    requests_total.inc()
    request_latency.observe(duration)

    logger.info(json.dumps({"features": req.features, "prediction": pred, "ms": round(duration * 1000, 2)}))

    if db_conn:
        try:
            db_conn.cursor().execute(
                "INSERT INTO predictions (features, prediction, duration_ms) VALUES (%s, %s, %s)",
                (json.dumps(req.features), pred, duration * 1000),
            )
        except Exception:
            pass

    return {"prediction": pred}
