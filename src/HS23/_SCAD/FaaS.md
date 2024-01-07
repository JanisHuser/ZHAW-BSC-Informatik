# FaaS (Function as a Service)

![Alt text](media/image-4.png)

- runs on a BaaS (Backend as a Service).
- allows to have specific functions or methods run in most programming langauges on a cloud provider.
- code is uploaded to the cloud provider

![Alt text](<media/Bildschirmfoto 2024-01-07 um 14.52.50.png>)


- "Cloud functions" insipired by "functional programming" style
- stateless & short-lived
- high elastic scalability
- event driven
- single function[ality] microservices
- implied pricing model: true pay per use

## Advantages

- Almost no idle periods
- small implementations
- fast startup graceful shutdown

## FaaS units

A single function acts as a **processing unit**. The function can be **triggered** (HTML GET/POST, ...). The processing unit can be implemnented in any programming language, most often NodeJs or Python is used.

![Alt text](media/image-5.png)

When having multiple of these functions are called a **App/Bundle**. The funtions in the bundle must be **uniquely identifiable by a name**.

**Input**

- Application specific: HTML, XML, JSON, ...
- Context parameters, direct protocol access (if supported)

**Output**

- Application specific: HTML, XML, JSON, ...
- state signaling, direct protocoll access (if supported)

**Model - Signature**
 
- Fixed ore registered name
- sync or async invocation
- parameters or via environment: event, context
- single return value

**Configuration**

- Runtime language & entry file
- Runtime parameters: memory, maximum duration, environment variables
- Packaging: artefacts, layers, libraries, isolation/containerisation, ...

## Encapsulation

![Alt text](media/image-6.png)

### Function Execution

Runs on provider supplied infrastructure (BaaS)

- Hidden / Non deterministic specs
- Function lifecycle (pooling, recycling, provisioned concurrenct)

### Function encapsulation

Provider supplied container image

- language runtime
- basic dependency libraries & framework

### Function

Developer supplied code

- "app/bundle": Advanced libraries & frameworks
- injection if supported
- layers


## Examples

### AWS lambda

```python
import logging
import os
from http import HTTPStatus
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

S3_BUCKET = os.environ['S3_BUCKET']


def lambda_handler(event, context):
    try:
        logger.info(f'Calling out to {S3_BUCKET} bucket to list objects')
        s3_client = boto3.client('s3')

        # Get all the objects from the bucket. Max 1000
        objects_in_bucket = s3_client.list_objects(Bucket=S3_BUCKET)

        logger.info('Found {} objects in the bucket. Printing a sample...'.format(len(objects_in_bucket['Contents'])))

        for key in objects_in_bucket['Contents'][:5]:
            logger.info('Found {} in bucket'.format(key['Key']))

    except Exception as e:  # Catch all for easier error tracing in logs
        logger.error(e, exc_info=True)
        raise Exception('Error occurred during execution')  # notify aws of failure

    return {
        "statusCode": HTTPStatus.OK.value
    }
```

### Azure 

```python
import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# A timer trigger function which repeats every 5 seconds and only accepts HTTP "GET" and "POST" requests.
@app.timer_trigger(schedule="5 * * * * *", arg_name="myTimer", methods=["GET", "POST"], run_on_startup=True,
              use_monitor=False) 
def TimerTrigger(myTimer: func.TimerRequest) -> None:
    
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')
```

## Converting existing architecture

Often, a conversion from a given architecture to a cloud architecture requires huge restructuring. This is because in traditional architecture, a monolitic architecture is required.


A existing design, where a centric server was used, is converted into a function based approach.

![Alt text](media/image-7.png)