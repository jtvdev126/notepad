# Create Lambda Function for Update Operation (UpdateNote)

import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Notes')

def lambda_handler(event,context):
    data = json.loads(event['body'])
    