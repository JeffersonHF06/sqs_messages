# SQS Messages Generator
This is a Python script that sends batches of messages to a SQS queue in AWS. It was created to emulate the amount of messages that a production environment receives and test functionalities on a staging environment sending 150 messages every 3 seconds.

## Requirements to run the script:
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
- Python 3 (I recommend to use [pyenv](https://github.com/pyenv/pyenv) to use any Python version).
- Permissions to access an AWS account and use SQS.

## How to use it
- Change the **message_body** with the message content you want to send and the **queue_name** with the name of the queue that will receive the messages.
- Login into AWS using the CLI of your computer.
- Run the next command: 
```python3 sqs.py```
