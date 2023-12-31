FROM python:3.9-alpine

RUN apk update && apk add curl gcc python3-dev build-base

RUN mkdir /app
WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . ./
CMD ["python3", "app.py"]

