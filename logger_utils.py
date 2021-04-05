import logging
import sys

logger = logging.getLogger('dynamo-to-sqs-aws-data-pipeline')
logger.setLevel(logging.INFO)

ch = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
ch.setLevel(logging.DEBUG)

fh = logging.FileHandler('/tmp/dynamo-to-sqs-aws-data-pipeline.log')
fh.setFormatter(formatter)
fh.setLevel(logging.ERROR)

logger.addHandler(ch)
logger.addHandler(fh)
