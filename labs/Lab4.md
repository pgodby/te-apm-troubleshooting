# Troubleshoot OTEL Manual Instrumentation

## Overview
In this lab exercise, you will troubleshoot unknown problems with a manually instrumented application.

## Prerequisites
Before you begin, you must first complete all of the previous lab exercises.

## Lab Exercise 4
1. The customer has implemented the suggested changes from the previous lab and has responded with the following information:

    > Thank you for the help! Can you help us understand why we are not seeing any spans for our REST requests from our Python application? We are using manual instrumentation and can see our manual spans. How do we capture the REST requests? We started the server with the following command: splunk-py-trace python Client.py

1. Return to the interactive shell attached to the **client** container (see Lab 1).
1. Investigate the issues with the client.

###### Tips
- For this exercise, you will only need to troubleshoot the **client** container.
- Review the [Help](Help.md) section for tips on working with the Docker containers.
- You do not need to modify any code.
- To stop the application, enter: **CTRL-C**

---

<details>
    <summary>Click to reveal the solution!</summary>

1. Stop the application: **CTRL-C**
1. Run the bootstrap script to enable instrumentation for installed packages.
    ```
    splunk-py-trace-bootstrap
    ```
1. Start the application.
    ```
    splunk-py-trace python Client.py
    ```
1. Verify the *client-python: GET HTTP GET* traces now appear in the Observability Cloud.
</details>

---
**Labs Exercises:** [1](Lab1.md) | [2](Lab2.md) | [3](Lab3.md) | 4 | [Help](Help.md)