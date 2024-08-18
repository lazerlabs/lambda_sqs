import json
import boto3
import os

def lambda_handler(event, context):
    sqs = boto3.client('sqs')
    queue_url = sqs.get_queue_url(QueueName='my-sqs-queue')['QueueUrl']

    try:
        # Calculate remaining time
        remaining_time = context.get_remaining_time_in_millis() / 1000  # Convert to seconds
        wait_time = min(20, max(1, int(remaining_time - 1)))  # Ensure wait time is between 1 and 20 seconds

        # Receive message
        response = sqs.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=1,
            WaitTimeSeconds=wait_time  # Dynamic wait time
        )
        
        if 'Messages' in response:
            message = response['Messages'][0]
            receipt_handle = message['ReceiptHandle']
            
            # Process the message (in this case, we're just returning it)
            message_body = message['Body']
            
            # Delete the message
            sqs.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=receipt_handle
            )
            
            return {
                'statusCode': 200,
                'body': message_body
            }
        else:
            return {
                'statusCode': 204,
                'body': 'No messages available'
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
