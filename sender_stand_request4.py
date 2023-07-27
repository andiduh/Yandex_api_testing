import configuration
import requests
import data
def post_new_user(body, headers):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
        json=body,  # тут тело
        headers=headers
    )  # а здесь заголовки

response = post_new_user(data.user_body, data.headers);
print(response.status_code)
print(response.json())