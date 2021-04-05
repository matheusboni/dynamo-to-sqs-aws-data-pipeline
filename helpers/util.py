from datetime import datetime
from typing import Union


class Util:

    @staticmethod
    def now() -> str:
        return datetime.now().isoformat()[:-3]

    @staticmethod
    def build_payload(item: dict) -> Union[dict, None]:
        user_id = item.get('userId')
        service_id = int(item.get('serviceId'))

        if user_id is not None and service_id is not None:
            return dict(
                userId=user_id,
                serviceId=service_id
            )
        else:
            return None
