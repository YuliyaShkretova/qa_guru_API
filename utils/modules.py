import requests
from jsonschema import validate

from utils.helper import load_json_schema, reqres_session


def register_user():
    r_user = {
        'email': 'eve.holt@reqres.in',
        'password': 'pistol'
    }
    return r_user


class ApiTest:
    def __init__(self, base_url):
        self.base_url = base_url

    def validate_response_200(self, response, schema):
        assert response.status_code == 200
        validate(instance=response.json(), schema=schema)

    def validate_response_400(self, response, schema):
        assert response.status_code == 400
        validate(instance=response.json(), schema=schema)

    @classmethod
    def validate_response_201(self, response, schema):
        assert response.status_code == 201
        validate(instance=response.json(), schema=schema)
        return response

    def validate_request(cls, request_data, schema, *args, **kwargs):
        validate(instance=request_data, schema=schema)

    #
    # def test_get_one_user_data(self, user_id):
    #     request_schema = load_json_schema('get_single_user.json')
    #     response_schema = load_json_schema('get_single_user.json')
    #
    #     url = f'{self.base_url}/users/{user_id}'
    #     response = reqres_session.get(url)
    #
    #     self.validate_response_200(response, response_schema)
    #
    #     request_data = {'id': user_id}
    #     self.validate_request(request_data, request_schema)
    @classmethod
    def validate_reponse_201(cls, response):
        pass




