import json

import allure
from jsonschema import validate

class ApiResponse:
    def __init__(self, base_url):
        self.base_url = base_url
        super().__init__()

    @staticmethod
    def validate_response_status(response_code, expected_status):
        with allure.step('Проверить код ответа'):
            assert response_code == expected_status


    @staticmethod
    def validate_response_schema(response_json, schema):
        with allure.step('Валидировать схему ответа'):
            validate(instance=response_json, schema=schema)

    @staticmethod
    def extract_response_data(response):
        response_code = response.status_code
        response_content = response.text
        try:
            response_json = response.json()
        except json.JSONDecodeError:
            response_json = None
        return response_code, response_json or response_content

