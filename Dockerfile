FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN apt-get update
RUN apt-get install python3-dev -y
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/