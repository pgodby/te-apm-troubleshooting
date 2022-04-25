# Troubleshoot the Splunk OTEL Collector

## Overview
In this lab exercise, you will troubleshoot unknown problems with the Splunk OpenTelemetry Collector.

## Prerequisites
Before you begin, you must first complete all of the previous lab exercises.

## Lab Exercise 2
1. A customer has contacted support with the following information:

    > We have manually instrumented a Python application using the OpenTelemetry and Splunk SDKs. This application submits REST requests to our server application. The server is a Node.js application that uses auto-instrumentation with the Splunk SDK. Both applications use the Splunk OTEL Collector to forward data to Splunk APM. While we believe we have the proper configuration in place, we are not seeing any data in Splunk APM except for our manual Python spans. Please help!

1. Return to the terminal window used to start the containers (see Lab 1).
1. Gather debug logs from the Splunk OTEL Collector.

###### Tips
- For this exercise, you will only need to work with the **splunk-otel-collector** container.
- Review the [Help](Help.md) section for tips on working with the Docker containers.

---

<details>
    <summary>Click to reveal the solution!</summary>

1. Copy the configuration file to your local machine.
    ```
    docker cp splunk-otel-collector:/etc/otel/collector/agent_config.yaml .
    ```
1. Using a text editor, [Enable Debug Logs](https://github.com/open-telemetry/opentelemetry-collector/blob/main/docs/troubleshooting.md#version-036-and-above).
1. Copy the configuration file back to the container.
    ```
    docker cp agent_config.yaml splunk-otel-collector:/etc/otel/collector/agent_config.yaml
    ```
1. Restart the container.
    ```
    docker restart splunk-otel-collector
    ```
1. Collect logs and debug logs
    ```
    docker logs splunk-otel-collector &> splunk-otel-collector.log
    ```
1. Review the logs and proceed to the next lab.
</details>

---
**Lab Exercises:** [1](Lab1.md) | [2](Lab2.md) | [3](Lab3.md) | [4](Lab4.md) | [Help](Help.md)