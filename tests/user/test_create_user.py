import requests

def test_create_user():
    url = "http://localhost:8080/api/v3/user"

    user_payload = {
    "id": 10,
    "username": "theUser",
    "firstName": "John",
    "lastName": "James",
    "email": "john@email.com",
    "password": "12345",
    "phone": "12345",
    "userStatus": 1
    }

    response = requests.post(url, json=user_payload)
    print("Status Code:", response.status_code)
    print("Response:", response.text)
