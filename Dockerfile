FROM python:3.11-slim

WORKDIR /calculadora

COPY app/ ./app/
COPY server.py .

EXPOSE 8080

CMD ["python", "server.py"]
