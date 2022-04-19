from time import time, sleep
from opentelemetry import trace
import requests

tracer = trace.get_tracer("te-apm")

# call the /api endpoint of the Node.JS server
def getAPI():
    span = tracer.start_span(name="/api", kind=trace.SpanKind.CLIENT)
    span.set_attribute("mykey", "myvalue")
    span.add_event("GET something")
    
    try:
        response = requests.get(url="http://server:3000/api")
        print("[" + str(response.status_code) + "] " + response.text)
    except requests.exceptions.RequestException as e:
        print("An error occurred. Retrying...")

    span.end()
    return

while True:
    getAPI()
    sleep(30 - time() % 30)