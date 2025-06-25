import boto3

sqs = boto3.client('sqs', region_name='us-east-1')  
queue_name = "shift-events-queue"

response = sqs.create_queue(
    QueueName=queue_name,
    Attributes={
        'VisibilityTimeout': '30'  
    }
)

print(f"Queue created: {response['QueueUrl']}")
