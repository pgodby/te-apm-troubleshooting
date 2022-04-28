# OpenTelemetry Instrumentation Troubleshooting

## Overview
This workshop will demonstrate how to troubleshoot issues that might be encountered while instrumenting applications for Splunk Application Performance Monitoring (APM). The lab exercises are designed to mimic potential support requests and will:

- Provide a short description of the problem
- Include a summary of the current state of the environment
- Present an opportunity for a technical support engineer to solve the problem
- Detail the steps to resolve the issue

**Note:** You will not be required to write or modify any code.

## Prerequisites
All lab exercises share the following set of requirements:

- Completed the Splunk Coach course: **O11y Support - OpenTelemetry Instrumentation Troubleshooting**
- Knowledge of OpenTelemetry and how it is used to send trace/span data to Splunk APM
- You have [git](https://git-scm.com/) installed to clone this repository
- You are a member of a Splunk APM enabled organization in the Splunk Observability Cloud and you have a valid access token from the organization

## Getting Started
Before you begin, you must complete the following steps:

1. Clone the GitHub repository
```
git clone https://github.com/pgodby/te-apm-troubleshooting
cd te-apm-troubleshooting
``` 

## Lab Exercises
In this workshop, you will deploy the base environment and then proceed with the lab exercises to troubleshoot OTEL instrumentation issues. After completing the lab exercises, you should have a better undertanding of the setup processes required for OTEL instrumented applications and how to send data to Splunk APM.

1. [Deploy the Base Environment](./labs/Lab1.md)
1. [Troubleshoot the Splunk OTEL Collector](./labs/Lab2.md)
1. [Troubleshoot OTEL Automatic Instrumentation](./labs/Lab3.md)
1. [Troubleshoot OTEL Manual Instrumentation](./labs/Lab4.md)