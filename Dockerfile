FROM python:3.9-slim

WORKDIR /app

COPY app.py /app/

RUN pip install nicegui

EXPOSE 8080

CMD ["python", "app.py"]
