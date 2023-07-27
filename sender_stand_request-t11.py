import configuration
import requests
import data
import sender_stand_request4
import sender_stand_request3

def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body

def test_1create_user_null_letter_in_first_name_get_success_response():
    user_body = get_user_body(data.name)
    user_response = sender_stand_request4.post_new_user(user_body, data.headers)
    assert user_response.status_code == 400

def test_2create_user_null_letter_in_first_name_get_success_response():
    user_body = get_user_body(data.name)
    user_response = sender_stand_request4.post_new_user(user_body, data.headers)
    assert user_response.json()["code"] == 400

def test_3create_user_null_letter_in_first_name_get_success_response():
    user_body = get_user_body(data.name)
    user_response = sender_stand_request4.post_new_user(user_body, data.headers)
    assert user_response.json()["message"] == "Не все необходимые параметры были переданы"
