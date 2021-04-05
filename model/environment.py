import os


class Environment:
    AWS_REGION = os.getenv("REGION")
    QUEUE_NAME = os.getenv("QUEUE_NAME")
    DYNAMO_TABLE = os.getenv("DYNAMO_TABLE")
