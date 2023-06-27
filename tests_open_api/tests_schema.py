from pprint import pprint

import requests
from jsonschema import validate
from curlify import to_curl

from helper import reqres_session, load_json_schema


def test_scheme_get_one_user_data():
    id = 2
    schema = load_json_schema('get_single_user.json')

    response = reqres_session.get(url='/users/', params={'id': id})

    assert response.status_code == 200
    validate(instance=response.json(), schema=schema)


def test_scheme_create_new_user():
    name = 'nameee'
    job = 'jooob'
    schema = load_json_schema('post_create_user.json')

    response = reqres_session.post(url='/users', json={'name': name, 'job': job})

    assert response.status_code == 201
    validate(instance=response.json(), schema=schema)


def test_scheme_delete_user():
    user_id = 2000

    response = reqres_session.delete(url='/users/', params={'user_id': user_id})

    assert response.status_code == 204
    assert response.text is ''


def test_scheme_patch_user():
    user_id = 45
    name = "111"
    job = "new york"
    schema = load_json_schema('patch_update_user.json')

    response = reqres_session.patch(url='/users/', params={'user_id': user_id}, json={'name': name, 'job': job})
    assert response.status_code == 200
    validate(instance=response.json(), schema=schema)


def test_scheme_register_200():
    email = 'eve.holt@reqres.in'
    password = 'pistol'

    schema = load_json_schema('post_register_200.json')

    response = reqres_session.post(url='/register', json={'email':email, 'password': password})
    assert response.status_code == 200
    validate(instance=response.json(), schema=schema)


def test_scheme_register_400():
    email = 'eve.holt@reqres.in'

    schema = load_json_schema('post_register_400.json')

    response = reqres_session.post(url='/register', json={'email': email})
    assert response.status_code == 400
    validate(instance=response.json(), schema=schema)

