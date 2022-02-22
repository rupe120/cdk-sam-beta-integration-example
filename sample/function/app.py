import json
import boto3
import os
import requests

#athena_workgroup = os.environ['ATHENA_WORKGROUP']
#athena_client = boto3.client('athena')

def lambda_handler(event, context):
    print(event)

    result = requests.get('https://api.github.com')
    print(result)

    return "Hi!"