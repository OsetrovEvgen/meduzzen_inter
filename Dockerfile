FROM python:3.8

COPY src /src

COPY requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

WORKDIR /src
