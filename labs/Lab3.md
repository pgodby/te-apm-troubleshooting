# Troubleshoot OTEL Automatic Instrumentation

## Overview
In this lab exercise, you will troubleshoot unknown problems with an automatically instrumented application.

## Prerequisites
Before you begin, you must first complete all of the previous lab exercises.

## Lab Exercise 3
1. The customer has implemented the suggested changes from the previous lab and has responded with the following information:

    > Thank you for the help! Can you now help us understand why we are not seeing any data from our Node.js server? We are using auto-instrumentation and started the server with the following command: node -r @splunk/otel/instrument index.js

1. Return to the interactive shell attached to the **server** container (see Lab 1).
1. Investigate the issues with the server.

###### Tips
- For this exercise, you will only need to troubleshoot the **server** container.
- Review the [Help](Help.md) section for tips on working with the Docker containers.
- You do not need to modify any code.
- To stop the application, enter: **CTRL-C**

---

<details>
    <summary>Click to reveal the solution!</summary>

1. Stop the application: **CTRL-C**
1. Review **package.json** for a list of currently installed packages.
    ```
    cat package.json
    ```
1. Install the missing instrumentation packages.
    ```
    npm install @opentelemetry/auto-instrumentations-node
    ```
1. Start the application.
    ```
    node -r @splunk/otel/instrument index.js
    ```
1. Verify the server now appears in the Observability Cloud.
</details>

---
**Lab Exercises:** [1](Lab1.md) | [2](Lab2.md) | [3](Lab3.md) | [4](Lab4.md) | [Help](Help.md)