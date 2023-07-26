import json
import logging
import os.path

import allure
import curlify
from allure_commons.types import AttachmentType
from requests import Session, Response


def load_json_schema(name: str):
    schema_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'schema', name)
    with open(schema_path) as schema:
        return json.loads(schema.read())


class CustomSession(Session):
    def __init__(self, base_url):
        self.base_url = base_url
        super().__init__()

    def request(self, method, url, *args, **kwargs) -> Response:
        response = super(CustomSession, self).request(method=method, url=self.base_url + url, *args, **kwargs)
        curl = curlify.to_curl(response.request)
        status_code = response.status_code
        total_data = f"'HTTP Status: {status_code} {curl}'"
        logging.info(total_data)
        with allure.step(f'{method} {url}'):
            if response.text is not None:
                allure.attach(body=total_data, name="Request curl", attachment_type=AttachmentType.TEXT,
                              extension='txt')
            else:
                allure.attach(body=total_data, name="Request curl", attachment_type=AttachmentType.JSON,
                              extension='json')

            return response


reqres_session = CustomSession('https://reqres.in/api')



