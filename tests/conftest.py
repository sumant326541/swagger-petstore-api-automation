import pytest
from dataclasses import dataclass
import requests
import json

@dataclass()
class Config():
    """
    Configuration class for pytest fixtures.
    This class can be used to define configuration parameters and utility funtion for the test suite.
    """
    # Add any configuration parameters you need here
    BASE_URL: str = "http://localhost:8080/api/v3/user"

@pytest.fixture(scope="function")
def test_config():
    """
    Fixture to provide configuration for the test suite.
    """
    return Config()

import pytest

@pytest.fixture(scope="function")
def user_payload():
    """
    Fixture to provide user payload for the test suite.
    """
    return {
        "id": 10,
        "username": "theUser",
        "firstName": "John",
        "lastName": "James",
        "email": "john@email.com",
        "password": "12345",
        "phone": "12345",
        "userStatus": 1
    }


@pytest.fixture(scope="function")
def create_user(user_payload, test_config):
    """
    Fixture to provide a function for creating a user.
    """
    def _create_user():
        response = requests.post(test_config.BASE_URL, json=user_payload)
        return response

    return _create_user

@pytest.fixture(scope="function")
def login_user(test_config):
    """
    Fixture to provide a function for logging in a user.
    """
    def _login_user(username, password):
        response = requests.get(test_config.BASE_URL + "/login"+f"?username={username}&password={password}")
        return response

    return _login_user

@pytest.fixture(scope="function")
def get_user(test_config):
    """
    Fixture to provide a function for getting a user.
    """
    def _get_user(user_id):
        response = requests.get(test_config.BASE_URL + f"/{user_id}")
        return response

    return _get_user

@pytest.fixture(scope="function")
def update_user(test_config):
    """
    Fixture to provide a function for updating a user.
    """
    def _update_user(user_id, user_payload):
        response = requests.put(test_config.BASE_URL + f"/{user_id}", json=user_payload)
        return response

    return _update_user

@pytest.fixture(scope="function")
def delete_user(test_config):
    """
    Fixture to provide a function for deleting a user.
    """
    def _delete_user(user_name):
        response = requests.delete(test_config.BASE_URL + f"/{user_name}")
        return response

    return _delete_user

@pytest.fixture(scope="function")
def logout_user(test_config):
    """
    Fixture to provide a function for logging out a user.
    """
    def _logout_user():
        response = requests.get(f"{test_config.BASE_URL}/logout")
        return response

    return _logout_user