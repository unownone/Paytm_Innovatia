# syntax=docker/dockerfile:1.1
FROM ubuntu:20.04
WORKDIR /code
RUN apt-get update -y && apt-get install python3-pip -y
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
COPY . .
CMD ["python","manage.py","runserver"]