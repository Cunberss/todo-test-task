FROM python:3.10

WORKDIR /app

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP=src/main.py
ENV FLASK_RUN_HOST=0.0.0.0