FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE=true

WORKDIR /app

SHELL ["/bin/bash", "-c"]

RUN useradd --create-home --shell /bin/bash fastapi && chown -R fastapi /app && \
    apt-get -y update && apt-get -y install curl && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt && pip cache purge
     
COPY --chown=fastapi:root main.py .

USER fastapi

CMD ["uvicorn","main:app", "--host", "0.0.0.0", "--log-level", "debug", "--reload"]