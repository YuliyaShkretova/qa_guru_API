import time
from pprint import pprint
from random import randint

import requests
from module import BASE_URL



def test_update_user_data_by_put():
    name = "morpheus"
    job = "zion resident"

    response = requests.put(
        url=BASE_URL + 'users/2',
        json={
            "name": name,
            "job": job}
    )

    assert response.status_code == 200
    assert response.json()['name'] == name
    assert response.json()['job'] == job
    json_data = response.json()
    assert 'updatedAt' in json_data
    pprint(response.json())


def test_update_user_data_patch():
    name = "morpheus"
    job = "zion resident"

    response = requests.patch(
        url=BASE_URL + 'users/2',
        json={
            "name": name,
            "job": job}
    )

    assert response.status_code == 200
    assert response.json()['name'] == name
    assert response.json()['job'] == job
    json_data = response.json()
    assert 'updatedAt' in json_data
    pprint(response.json())


def test_get_full_data_of_user():
    response = requests.get(BASE_URL + 'users/12'
                            )
    assert response.status_code == 200
    assert response.json()['data']['id'] == 12
    pprint(response.json())


def test_user_registration_successful():
    email = 'eve.holt@reqres.in'
    password = 'pistol'
    response = requests.post(BASE_URL+'register',
        {
            "email": email,
            "password": password
        }
    )
    assert response.status_code == 200
    assert response.json()['id'] is not None
    assert response.json()['token'] is not None
    # assert response.json()['id'] == 4
    # assert response.json()['token'] == 'QpwL5tke4Pnpja7X4'
    pprint(response.json())


def test_create_user_successful():
    name = 'dfjkdfdgf'
    job = 'dfgfghgjh'
    response = requests.post(BASE_URL + 'users',
                             {
                                 "name": name,
                                 "job": job
                             }
                             )
    assert response.status_code == 201
    assert response.json()['name'] == name
    assert response.json()['job'] == job
    assert 'createdAt' in response.json()
    pprint(response.json())


def test_delete_user():
    response = requests.delete(BASE_URL + 'users/12')
    assert response.status_code == 204
    assert response.text == ''


def test_get_uncreated_user():
    user = requests.get(BASE_URL + 'unknown')
    data = user.json()
    user_list = [item['id'] for item in data['data']]
    a = user_list[-1]+1
    print(a)
    user_id = randint(a, 100)
    response = requests.get(BASE_URL + 'unknown/' + f'{user_id}')
    assert response.status_code == 404
    assert response.json() == {}
    pprint(user_id)
    pprint(response.json())


def test_unsuccessful_login():
    email = 'gcg@gfgnf.rwe'

    response = requests.post(
        url=BASE_URL + 'login',
        json={
            "email": email}
    )
    assert response.status_code == 400
    assert response.json().get('error') == "Missing password"
    pprint(response.json())


def test_unsuccessful_registration():
    email = 'gcg@gfgnf.rwe'

    response = requests.post(
        url=BASE_URL + 'register',
        json={
            "email": email}
    )
    assert response.status_code == 400
    assert response.json().get('error') == "Missing password"
    pprint(response.json())


def test_delay_reply():
    time_delay = 10
    start_time = time.time()
    response = requests.get(
        BASE_URL + 'users/', params={'delay': time_delay})
    end_time = time.time()
    assert response.status_code == 200
    assert (end_time - start_time) >= time_delay
    pprint(response.json())
