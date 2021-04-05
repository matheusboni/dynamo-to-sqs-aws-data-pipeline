import json
from datetime import datetime

import boto3
from boto3.dynamodb.conditions import Attr

from aws.queue_service import QueueService
from helpers.util import Util as util
from logger_utils import logger
from model.environment import Environment as envs


class Service:
    def __init__(self):
        self.__dynamo = boto3.resource("dynamodb", region_name=envs.AWS_REGION)
        self.__table = self.__dynamo.Table(envs.DYNAMO_TABLE)
        self.__queue_service = QueueService()

    def find_expired_subscriptions_then_process(self, now: str) -> None:
        subscriptions = self.__table.scan(FilterExpression=Attr('nextPaymentDate').lte(now))
        items = subscriptions['Items']
        if len(items) > 0:
            self.__process(items)

        while 'LastEvaluatedKey' in subscriptions:
            subscriptions = self.__table.scan(
                FilterExpression=Attr('nextPaymentDate').lte(now),
                ExclusiveStartKey=subscriptions['LastEvaluatedKey']
            )
            items = subscriptions['Items']
            if len(items) > 0:
                self.__process(items)

    def __process(self, items: list) -> None:
        for item in items:
            payload: dict = util.build_payload(item)

            if payload is not None:
                self.__queue_service.send_message(json.dumps(payload))
            else:
                logger.warn("Invalid payload!")
