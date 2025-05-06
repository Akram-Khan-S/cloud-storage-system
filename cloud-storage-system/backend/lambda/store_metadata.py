
import json
import boto3
import os
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table_name = os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    data = json.loads(event['body'])
    item = {
        'file_name': data['file_name'],
        'user_id': data['user_id'],
        'timestamp': datetime.utcnow().isoformat()
    }

    table.put_item(Item=item)

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Metadata stored'})
    }
