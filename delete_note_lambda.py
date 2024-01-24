# Create Lambda Function for Delete Operation (DeleteNote)

import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Notes')

def lambda_handler(event,context):
    note_id = event['pathParameters']['note_id']

    table.delete_item(
        Key={
            'note_id': note_id
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Note deleted successfully.')
    }