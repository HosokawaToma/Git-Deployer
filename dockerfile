FROM python:3.10.17

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY src/ src/
COPY config.yaml config.yaml

CMD ["python", "src/main.py"]
