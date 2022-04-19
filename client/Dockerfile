FROM python:latest

WORKDIR /app
COPY Client.py ./

RUN pip install requests
RUN pip install opentelemetry-api
RUN pip install splunk-opentelemetry[all]

CMD ["tail","-f","/dev/null"]