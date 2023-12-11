FROM python:3.8-slim

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn==20.1.0
EXPOSE 5000

ENV IP 127.0.0.1

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--env", "IP=$IP", "app:app"]