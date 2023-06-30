import boto3
import uuid
import time
import json

# Create a batch with 10 messages
def create_batch():
    message_body = { "Body": "Message" }
    messages = []
    for x in range(0, 10):
        messages.append(
            {
                'Id': str(uuid.uuid4()),
                'MessageBody': json.dumps(message_body)
            }
        )
    return messages

# Define the queue URL and messages to send
queue_name = 'queue_name'
messages = create_batch()
sqs = boto3.client('sqs')

# Send the messages in batches
for x in range(0, 15):
    response = sqs.send_message_batch(
        QueueUrl=queue_name,
        Entries=messages
    )

    print(response)

    time.sleep(3)
