import json
import boto3
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    sqs = boto3.client('sqs')
    queue_url = sqs.get_queue_url(QueueName='ibeam-sqs-queue')['QueueUrl']
    
    message = event['body']
    
    try:
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=message,
            MessageAttributes={
                'MessageTTL': {
                    'DataType': 'Number',
                    'StringValue': '300'
                }
        )

        logger.info(f"Message sent successfully. MessageId: {response['MessageId']}")

        return {
            'statusCode': 200,
            'body': 'Message sent successfully'
        }
    except Exception as e:
        logger.error(f"Error sending message: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }

