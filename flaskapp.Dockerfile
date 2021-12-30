FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE=true

WORKDIR /app

SHELL ["/bin/bash", "-c"]

RUN useradd --create-home --shell /bin/bash flask && chown -R flask /app && \
    apt-get -y update && apt-get -y install curl && \
    rm -rf /var/lib/apt/lists/*

COPY --chown=flask flask_app/requirements.txt requirements.txt

USER flask

RUN python3 -m venv venv && source venv/bin/activate && \
    pip install -r requirements.txt && pip cache purge
     

COPY --chown=flask:root flask_app/app.py .

CMD [ "venv/bin/python", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000"]
