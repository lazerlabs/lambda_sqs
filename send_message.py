import json
import boto3
import os

def lambda_handler(event, context):
    sqs = boto3.client('sqs')
    queue_url = sqs.get_queue_url(QueueName='my-sqs-queue')['QueueUrl']

    message = event['body']
    
    try:
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=message
        )
        return {
            'statusCode': 200,
            'body': json.dumps('Message sent successfully')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }

