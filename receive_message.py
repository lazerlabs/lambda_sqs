import json
import boto3
import os

def lambda_handler(event, context):

    max_wait_time = 20  # Maximum wait time for long polling

    sqs = boto3.client('sqs')
    queue_url = os.environ['SQS_QUEUE_URL']

    # Calculate remaining time
    remaining_time = context.get_remaining_time_in_millis() / 1000  # Convert to seconds
    wait_time = min(max_wait_time, max(1, int(remaining_time - 1)))  # Ensure wait time is between 1 and 20 seconds

    while True:
        try:
            # Receive message with long polling
            response = sqs.receive_message(
                QueueUrl=queue_url,
                MaxNumberOfMessages=1,
                WaitTimeSeconds=wait_time  # Dynamic wait time (up to 20 seconds)
            )
            
            if 'Messages' in response:
                message = response['Messages'][0]
                receipt_handle = message['ReceiptHandle']
                
                # Process the message (in this case, we're just returning it)
                message = json.loads(message['Body'])
                code = message['code']
                
                # Delete the message from the queue after processing
                sqs.delete_message(
                    QueueUrl=queue_url,
                    ReceiptHandle=receipt_handle
                )
                
                return {
                    'statusCode': 200,
                    'body': code
                }
            else:
                # No messages available after polling
                if wait_time >= max_wait_time:
                    return {
                        'statusCode': 204,
                        'body': 'No messages available'
                    }
        except Exception as e:
            if wait_time >= max_wait_time:
                return {
                    'statusCode': 500,
                    'body': f'Error: {str(e)}'
                }
