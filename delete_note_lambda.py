# Create Lambda Function for Delete Operation (DeleteNote)

import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Notes')

