FROM python:3.11-slim

WORKDIR app

COPY service_stt/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


COPY shared ./shared
COPY service_stt ./service_stt

ENV PYTHONPATH=/app


CMD ["python","service_stt/main.py"]