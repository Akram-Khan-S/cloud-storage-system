
import json
import boto3
import os
import uuid
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = os.environ['BUCKET_NAME']
    file_name = str(uuid.uuid4()) + ".pdf"

    try:
        presigned_url = s3.generate_presigned_url(
            'put_object',
            Params={'Bucket': bucket_name, 'Key': file_name},
            ExpiresIn=3600
        )
        return {
            'statusCode': 200,
            'body': json.dumps({'url': presigned_url, 'file_name': file_name})
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
