FROM python:3-slim
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/

RUN apt-get update
RUN apt-get install -y gdal-bin netcat

RUN pip install pipenv
RUN pipenv install --system --deploy