import allure
from utils.helper import load_json_schema, reqres_session
from utils.module import ApiResponse


def allure_decoration_steps(func):
    def wrapper(*args, **kwargs):
        return wrapper(*args, **kwargs)

    return func


@allure.tag("function")
@allure.label("owner", "Yuliya Shkretova")
@allure.feature("Tests for API")
@allure.link("https://reqres.in/")
@allure.title("Create new user, POST")
@allure.severity(severity_level='HIGH')
@allure_decoration_steps
def test_scheme_create_new_user():
    data = {'name': 'nameee', 'job': 'jooob'}
    schema = load_json_schema('post_create_user.json')

    response = reqres_session.post(url='/users', json=data)
    response_code, response_schema = ApiResponse.extract_response_data(response)
    ApiResponse.validate_response_status(response_code, 201)
    ApiResponse.validate_response_schema(response_schema, schema)
    assert response.json()['name'] == 'nameee'
    assert response.json()['job'] == 'jooob'


@allure.tag("function")
@allure.label("owner", "Yuliya Shkretova")
@allure.feature("Tests for API")
@allure.link("https://reqres.in/")
@allure.title("Update user, PATCH")
@allure.severity(severity_level='HIGH')
@allure_decoration_steps
def test_scheme_patch_user():
    user = {'user_id': 45}
    data = {'name': "111", 'job': "new york"}
    schema = load_json_schema('patch_update_user.json')

    response = reqres_session.patch(url='/users/', params=user, json=data)
    response_code, response_schema = ApiResponse.extract_response_data(response)
    ApiResponse.validate_response_status(response_code, 200)
    ApiResponse.validate_response_schema(response_schema, schema)

    assert response.json()['name'] == '111'
    assert response.json()['job'] == 'new york'


@allure.tag("function")
@allure.label("owner", "Yuliya Shkretova")
@allure.feature("Tests for API")
@allure.link("https://reqres.in/")
@allure.title("Unsuccessful login, POST")
@allure.severity(severity_level='HIGH')
@allure_decoration_steps
def test_scheme_login_400():
    data = {'email': 'peter@klaven'}

    schema = load_json_schema('post_reg_400.json')

    response = reqres_session.post(url='/login', json=data)
    response_code, response_schema = ApiResponse.extract_response_data(response)
    ApiResponse.validate_response_status(response_code, 400)
    ApiResponse.validate_response_schema(response_schema, schema)


@allure.tag("function")
@allure.label("owner", "Yuliya Shkretova")
@allure.feature("Tests for API")
@allure.link("https://reqres.in/")
@allure.title("Get list, GET")
@allure.severity(severity_level='HIGH')
@allure_decoration_steps
def test_scheme_get_list():
    schema = load_json_schema('get_list.json')

    response = reqres_session.get(url='/unknown')
    response_code, response_schema = ApiResponse.extract_response_data(response)
    ApiResponse.validate_response_status(response_code, 200)
    ApiResponse.validate_response_schema(response_schema, schema)


@allure.tag("function")
@allure.label("owner", "Yuliya Shkretova")
@allure.feature("Tests for API")
@allure.link("https://reqres.in/")
@allure.title("Delete user, DELETE")
@allure.severity(severity_level='HIGH')
@allure_decoration_steps
def test_scheme_delete_user():
    user = {'user_id': 2}
    response = reqres_session.delete(url='/users/', params=user)
    response_code, response_schema = ApiResponse.extract_response_data(response)
    ApiResponse.validate_response_status(response_code, 204)

