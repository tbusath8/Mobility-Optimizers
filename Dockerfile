FROM python:3.9



WORKDIR /app
COPY requirements.txt /app

RUN set -ex && \
    pip install -r requirements.txt

COPY . /app

EXPOSE 8050
CMD ["python", "app.py"]