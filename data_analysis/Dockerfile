FROM python:3.11-slim

WORKDIR /app

COPY data_analysis/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY data_analysis ./data_analysis
COPY shared ./shared

ENV PYTHONPATH=/app

CMD ["python","./data_analysis/main.py"]