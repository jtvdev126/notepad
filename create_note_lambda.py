# Create Lambda Function for Create Operation (CreateNote)

import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Notes')

def lambda_handler(event, context):
    data = json.loads(event['body'])

    table.put_item(
        Item={
            'note_id': data['note_id'],
            'content': data['content']
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Note created successfully!')
    }