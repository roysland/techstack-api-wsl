#FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
# COPY ./ /app

FROM python:3.7


EXPOSE 80
#COPY ./ /app
RUN pip install fastapi uvicorn
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
