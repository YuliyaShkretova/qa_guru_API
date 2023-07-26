import allure
from jsonschema import validate
from utils.helper import load_json_schema, reqres_session
from utils.modules import register_user


def allure_decoration_steps(func):
    def wrapper(*args, **kwargs):
        return wrapper(*args, **kwargs)

    return func


@allure.tag("function")
@allure.label("owner", "Yuliya Shkretova")
@allure.feature("Tests for API")
@allure.link("https://reqres.in/")
@allure.title("test_scheme_get_one_user_data")
@allure.severity(severity_level='HIGH')
@allure_decoration_steps
def test_scheme_get_one_user_data():
    id = 2
    schema = load_json_schema('get_single_user.json')

    response = reqres_session.get(url='/users/', params={'id': id})

    assert response.status_code == 200
    validate(instance=response.json(), schema=schema)


@allure.tag("function")
@allure.label("owner", "Yuliya Shkretova")
@allure.feature("Tests for API")
@allure.link("https://reqres.in/")
@allure.title("test_scheme_create_new_user")
@allure.severity(severity_level='HIGH')
@allure_decoration_steps
def test_scheme_create_new_user():
    name = 'nameee'
    job = 'jooob'
    schema = load_json_schema('post_create_user.json')

    response = reqres_session.post(url='/users', json={'name': name, 'job': job})

    assert response.status_code == 201
    validate(instance=response.json(), schema=schema)
    return response


@allure.tag("function")
@allure.label("owner", "Yuliya Shkretova")
@allure.feature("Tests for API")
@allure.link("https://reqres.in/")
@allure.title("test_scheme_delete_user")
@allure.severity(severity_level='HIGH')
@allure_decoration_steps
def test_scheme_delete_user():
    user_id = 2000

    response = reqres_session.delete(url='/users/', params={'user_id': user_id})

    assert response.status_code == 204
    assert response.text is ''


@allure.tag("function")
@allure.label("owner", "Yuliya Shkretova")
@allure.feature("Tests for API")
@allure.link("https://reqres.in/")
@allure.title("test_scheme_patch_user")
@allure.severity(severity_level='HIGH')
@allure_decoration_steps
def test_scheme_patch_user():
    user_id = 45
    name = "111"
    job = "new york"
    schema = load_json_schema('patch_update_user.json')

    response = reqres_session.patch(url='/users/', params={'user_id': user_id}, json={'name': name, 'job': job})
    assert response.status_code == 200
    validate(instance=response.json(), schema=schema)


@allure.tag("function")
@allure.label("owner", "Yuliya Shkretova")
@allure.feature("Tests for API")
@allure.link("https://reqres.in/")
@allure.title("test_scheme_register_200")
@allure.severity(severity_level='HIGH')
@allure_decoration_steps
def test_scheme_register_200():
    schema = load_json_schema('post_register_200.json')
    response = reqres_session.post(url='/register', json=register_user())
    assert response.status_code == 200
    # assert response.json() == register_user()
    validate(instance=response.json(), schema=schema)


@allure.tag("function")
@allure.label("owner", "Yuliya Shkretova")
@allure.feature("Tests for API")
@allure.link("https://reqres.in/")
@allure.title("test_scheme_register_400")
@allure.severity(severity_level='HIGH')
@allure_decoration_steps
def test_scheme_register_400():
    email = 'eve.holt@reqres.in'

    schema = load_json_schema('post_reg_400.json')

    response = reqres_session.post(url='/register', json={'email': email})
    assert response.status_code == 400
    validate(instance=response.json(), schema=schema)


@allure.tag("function")
@allure.label("owner", "Yuliya Shkretova")
@allure.feature("Tests for API")
@allure.link("https://reqres.in/")
@allure.title("test_scheme_login_400")
@allure.severity(severity_level='HIGH')
@allure_decoration_steps
def test_scheme_login_400():
    email = 'peter@klaven'

    schema = load_json_schema('post_reg_400.json')

    response = reqres_session.post(url='/login', json={'email': email})
    assert response.status_code == 400
    validate(instance=response.json(), schema=schema)


@allure.tag("function")
@allure.label("owner", "Yuliya Shkretova")
@allure.feature("Tests for API")
@allure.link("https://reqres.in/")
@allure.title("test_scheme_get_list")
@allure.severity(severity_level='HIGH')
@allure_decoration_steps
def test_scheme_get_list():
    schema = load_json_schema('get_list.json')

    response = reqres_session.get(url='/unknown')
    assert response.status_code == 200
    validate(instance=response.json(), schema=schema)


@allure.tag("function")
@allure.label("owner", "Yuliya Shkretova")
@allure.feature("Tests for API")
@allure.link("https://reqres.in/")
@allure.title("test_scheme_single")
@allure.severity(severity_level='HIGH')
@allure_decoration_steps
def test_scheme_single():
    id = 2
    schema = load_json_schema('get_single.json')

    response = reqres_session.get(url='/unknown/', params={'id': id})
    assert response.status_code == 200
    validate(instance=response.json(), schema=schema)


