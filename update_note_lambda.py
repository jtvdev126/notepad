# Create Lambda Function for Update Operation (UpdateNote)

import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Notes')

def lambda_handler(event,context):
    data = json.loads(event['body'])
    note_id = event['pathParameters']['note_id']

    table.update_item(
        Key={
            'note_id': note_id
        },
        UpdateExpression='SET content = :content',
        ExpressionAttributeValues={
            ':content':data['content']
        }
    )