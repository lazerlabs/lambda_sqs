# lambda-sqs

This project demonstrates a serverless application using AWS Lambda and Amazon SQS (Simple Queue Service). It includes two Lambda functions: one for sending messages to an SQS queue, and another for receiving messages from the queue.

## Project Structure

- `send_message.py` - Lambda function for sending messages to SQS
- `receive_message.py` - Lambda function for receiving messages from SQS
- `template.yaml` - SAM template defining the application's AWS resources
- `events/` - Sample events for testing the Lambda functions
- `tests/` - Unit tests for the application code

## Prerequisites

- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
- [Python 3.11](https://www.python.org/downloads/)
- [Docker](https://hub.docker.com/search/?type=edition&offering=community)
- AWS account and configured AWS CLI

## Deployment

1. Build the application:
   ```
   sam build --use-container
   ```

2. Deploy the application:
   ```
   sam deploy --guided
   ```

   Follow the prompts to set up your deployment configuration.

## Usage

After deployment, you'll receive two API Gateway endpoints:

- SendMessageApi: For sending messages to the SQS queue
- ReceiveMessageApi: For receiving messages from the SQS queue

To send a message:
```
curl -X POST https://your-send-api-endpoint/Prod/send/ -H "Content-Type: application/json" -d '{"message": "Hello, SQS!"}'
```

To receive a message:
```
curl https://your-receive-api-endpoint/Prod/receive/
```

## Local Testing

Test the functions locally using SAM CLI:

```
sam local invoke SendMessageFunction --event events/send_event.json
sam local invoke ReceiveMessageFunction --event events/receive_event.json
```

Start a local API for testing:

```
sam local start-api
```

## Monitoring

View Lambda function logs:

```
sam logs -n SendMessageFunction --stack-name "lambda-sqs" --tail
sam logs -n ReceiveMessageFunction --stack-name "lambda-sqs" --tail
```

## Cleanup

To remove all resources created by this project:

```
sam delete --stack-name "lambda-sqs"
```

## Resources

- [AWS SAM Developer Guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)
- [Amazon SQS Documentation](https://docs.aws.amazon.com/sqs/index.html)
- [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
```
