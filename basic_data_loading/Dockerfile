FROM python:3.11-slim

WORKDIR app

COPY basic_data_loading/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY basic_data_loading ./basic_data_loading
COPY shared ./shared

ENV PYTHONPATH=/app

CMD ["python","./basic_data_loading/main.py"]