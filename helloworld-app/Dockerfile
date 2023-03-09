FROM python:3.8-slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /opt/microservices
COPY app.py ./

EXPOSE 5000

ARG service_version
ENV SERVICE_VERSION ${service_version:-v1}

CMD ["python", "app.py"]
