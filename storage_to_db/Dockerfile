FROM python:3.11-slim

WORKDIR app

COPY storage_to_db/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY storage_to_db ./storage_to_db
COPY shared ./shared

ENV PYTHONPATH=/app

CMD ["python","./storage_to_db/main.py"]

