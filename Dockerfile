FROM python:3.8

COPY ./src /src

COPY ./requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

WORKDIR /src/healthcheck

ENTRYPOINT ["uvicorn", "app:app", "--port", "8000", "--host", "0.0.0.0"]



