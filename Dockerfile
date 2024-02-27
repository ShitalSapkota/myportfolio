FROM ubuntu:latest
FROM python:3.11-bullseye
LABEL authors="shital sapkota"
WORKDIR myportfolio
COPY . /myportfolio

EXPOSE 8000
RUN pip install -U -r requirements.txt
CMD ["python", "myportfolio/manage.py", "runserver", "0.0.0.0:8000"]