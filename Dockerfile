#FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
# COPY ./ /app

FROM python:3.7

RUN pip install
EXPOSE 80
COPY ./ /app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
