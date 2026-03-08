# Финальное задание по MLOps

## Этап 1 — MLflow

Запуск:
```
cd mlflow
cp .env.example .env
docker compose up -d
```

UI тут: http://localhost:5000

Запуск эксперимента:
```
python log_experiment.py
```

Скриншот эксперимента

<img src="https://raw.githubusercontent.com/mvplatonova/hse_mlops_final/master/mlflow/experiment_list.png" alt="текст" width="750"/>

---

## Этап 2 — Airflow

Запуск:
```
cd airflow
cp .env.example .env
docker compose up -d
```

UI тут: http://localhost:8080 (admin / admin)

Скриншот запуска:

<img src="https://raw.githubusercontent.com/mvplatonova/hse_mlops_final/master/airflow/succes_dag.png" alt="текст" width="750"/>

---

## Этап 3 — LakeFS

Запуск:
```
cd lakefs
cp .env.example .env
docker compose up -d
```

MinIO: http://localhost:9001 (minioadmin / minioadmin) — создать bucket `lakefs-bucket`

LakeFS: http://localhost:8001 — создать репозиторий, ветку `dev`, загрузить файл, сделать commit

Скриншоты UI:

<img src="https://raw.githubusercontent.com/mvplatonova/hse_mlops_final/master/lakefs/repo.png" alt="текст" width="750"/>

<img src="https://raw.githubusercontent.com/mvplatonova/hse_mlops_final/master/lakefs/comit.png" alt="текст" width="750"/>

---

## Этап 4 — JupyterHub

Запуск:
```
cd jupyterhub
docker compose up -d
```

UI тут: http://localhost:8000 (admin / admin)

Скриншот ноутбука:

<img src="https://raw.githubusercontent.com/mvplatonova/hse_mlops_final/master/jupyterhub/screenshot.png" alt="текст" width="750"/>

---

## Этап 5 — ML-сервис

Запуск:
```
cd ml-service
cp .env.example .env
docker compose up -d
```

Запрос predict можно сделать через UI (http://localhost:8080/docs) 

Cкриншот вызова predict

<img src="https://raw.githubusercontent.com/mvplatonova/hse_mlops_final/master/ml-service/predict.png" alt="текст" width="750"/>


## Этап 6 — Мониторинг

Используем ml-service из этапа 5

Prometheus: http://localhost:9090
Grafana: http://localhost:3000 (admin / admin) → datasource Prometheus (`http://prometheus:9090`) → дашборд с метрикой `predict_requests_total`

Скриншоты из Prometheus и Grafana

<img src="https://raw.githubusercontent.com/mvplatonova/hse_mlops_final/master/ml-service/prometeus_status.png" alt="текст" width="750"/>

<img src="https://raw.githubusercontent.com/mvplatonova/hse_mlops_final/master/ml-service/grafana.png" alt="текст" width="750"/>


## Этап 7 — Kubernetes

Манифесты в папке `k8s/`: deployment, service, ingress


## Этап 8 — Helm

```
helm lint helm/
helm install ml-service helm/
```

Скриншот:

<img src="https://raw.githubusercontent.com/mvplatonova/hse_mlops_final/master/helm/image.png" alt="текст" width="750"/>

---

## Этап 9 — MLflow Prompt Storage

Используем mlflow из этапа 1

Запуск:
```
python mlflow/create_prompts.py
```

Скриншоты промптов:

<img src="https://raw.githubusercontent.com/mvplatonova/hse_mlops_final/master/mlflow/prompts.png" alt="текст" width="750"/>

<img src="https://raw.githubusercontent.com/mvplatonova/hse_mlops_final/master/mlflow/prompt_inner.png" alt="текст" width="750"/>
