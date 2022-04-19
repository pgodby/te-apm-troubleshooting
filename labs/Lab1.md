# Deploy the Base Environment

## Overview
In this lab exercise, you will deploy a set of Docker containers that are required for the troubleshooting exercises. Environment variables for a container can be set in the specified configuration file (located in the [/base](../base) directory).

| Container | Config File | Description |
| --- | --- | --- |
| splunk-otel-collector | collector.env | The Splunk OpenTelemetry Collector instance that will be used to forward trace data to Splunk Application Performance Monitoring (APM). This instance is running in agent mode and will provide services for all instrumented applications. |
| server | server.env | An auto-instrumented Node.js server application |
| client | client.env | A manually instrumented Python client application |

## Prerequisites
To complete this exercise, you must have the following software installed:
- [Docker Engine](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/) 

## Lab Exercise 1
For this lab exercise, you should only make the changes specified below. The troubleshooting exercises that follow are designed to simulate problems in a customer environment. If you have already noticed incorrect or missing settings in this repository, just ignore it (for now)!

1. If Zscaler is running on your machine, turn it off. It will break connectivity between the OTEL Collector and the Observability Cloud.
1. Specify the Splunk Observability Cloud realm and access token you will use in the file named **collector.env**
    ```
    SPLUNK_ACCESS_TOKEN=<your_token>
    SPLUNK_REALM=<your_realm>
    ```
1. Specify the Splunk Observability Cloud deployment you will use in the files named **server.env** and **client.env**. This value should be the same in both files.
    ```
    OTEL_RESOURCE_ATTRIBUTES=deployment.environment=<your_deployment>
    ```
1. In a terminal window, enter the following commands to build and start the Docker containers. Leave this window open.
    ```
    cd /te-apm-troubleshooting/base
    docker-compose up --build -d
    ```
1. In a *new* terminal window, start the server application with the following commands. Leave this window open.
    ```
    docker exec -it server sh
    node -r @splunk/otel/instrument index.js
    ```
1. In a *new* terminal window, start the client application with the following commands. Leave this window open.
    ```
    docker exec -it client sh
    splunk-py-trace python Client.py
    ```
1. In the Splunk Observability Cloud, review your deployment for activity. The Python client will send a REST request to the Node.js server once every 30 seconds. It might take several minutes for the data to fully appear. You may not see everything you would normally expect to see. This is intended.
1. Review the [Help](Help.md) section for tips on working with the Docker containers.

---
**Labs Exercises:** 1 | [2](Lab2.md) | [3](Lab3.md) | [4](Lab4.md) | [Help](Help.md)