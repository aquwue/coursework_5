FROM python:3.8.5

ENV FLASK_APP help_files.app:app

WORKDIR /opt

COPY requirements.txt .


RUN python -m pip install --upgrade pip && pip install -r requirements.txt

COPY help_files help_files