import boto3

from logger_utils import logger
from model.environment import Environment as envs


class QueueService:

    def __init__(self):
        self.__sqs_client = boto3.resource('sqs', region_name=envs.AWS_REGION)
        self.__queue = self.__sqs_client.get_queue_by_name(QueueName=envs.QUEUE_NAME)

    def send_message(self, obj):
        try:
            logger.info("Sending: {} to queue: {}".format(obj, self.__queue))

            self.__queue.send_message(MessageBody=obj)

        except Exception as e:
            logger.exception("Error sending message: {}".format(obj), e)
