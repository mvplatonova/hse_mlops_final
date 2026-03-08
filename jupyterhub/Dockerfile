FROM python:3.11-slim

RUN apt-get update && apt-get install -y nodejs npm
RUN pip install jupyterhub jupyterlab configurable-http-proxy
RUN useradd -m -s /bin/bash admin

COPY jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

WORKDIR /srv/jupyterhub
EXPOSE 8000

CMD ["jupyterhub", "-f", "/srv/jupyterhub/jupyterhub_config.py"]
