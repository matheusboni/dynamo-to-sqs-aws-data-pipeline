from helpers.util import Util as util
from logger_utils import logger
from service.service import Service

service = Service()


def main() -> None:

    try:
        now: str = util.now()
        logger.info("Data Pipeline Started at: {}".format(now))

        service.find_expired_subscriptions_then_process(now)

        logger.info("Data Pipeline Finished at: {}".format(util.now()))
    except Exception as e:
        logger.exception("Unknown and unexpected exception!", e)


if __name__ == '__main__':
    main()
