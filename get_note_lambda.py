# Create Lambda Function for Read Operation (GetNote)

import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Notes')

def lambda_handler(event, context):
    note_id = event['pathParameters']['note_id']

    response = table.get_item(
        Key={
            'note_id': note_id
        }
    )
    
    item = response.get('Item', {})

    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }
