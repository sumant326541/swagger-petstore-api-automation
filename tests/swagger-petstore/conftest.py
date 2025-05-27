import pytest
from dataclasses import dataclass
import requests
import os
import json

@dataclass()
class Config():
    """
    Configuration class for pytest fixtures.
    This class can be used to define configuration parameters and utility funtion for the test suite.
    """
    # Base URL and end point for the user API
    BASE_URL: str = os.getenv("BASE_URL", "http://localhost:8080/api/v3")
    USER_ENDPOINT: str = "user"
 
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
        url = f"{test_config.BASE_URL}/{test_config.USER_ENDPOINT}"
        response = requests.post(url, json=user_payload)
        return response

    return _create_user

@pytest.fixture(scope="function")
def login_user(test_config):
    """
    Fixture to provide a function for logging in a user.
    """
    def _login_user(username, password):
        url = f"{test_config.BASE_URL}/{test_config.USER_ENDPOINT}/login?username={username}&password={password}"
        response = requests.get(url)
        return response

    return _login_user

@pytest.fixture(scope="function")
def get_user(test_config):
    """
    Fixture to provide a function for getting a user.
    """
    def _get_user(user_name):
        url = f"{test_config.BASE_URL}/{test_config.USER_ENDPOINT}/{user_name}"
        response = requests.get(url)
        return response

    return _get_user

@pytest.fixture(scope="function")
def update_user(test_config):
    """
    Fixture to provide a function for updating a user.
    """
    def _update_user(user_name, user_payload):
        url = f"{test_config.BASE_URL}/{test_config.USER_ENDPOINT}/{user_name}"
        response = requests.put(url, json=user_payload)
        return response

    return _update_user

@pytest.fixture(scope="function")
def delete_user(test_config):
    """
    Fixture to provide a function for deleting a user.
    """
    def _delete_user(user_name):
        url = f"{test_config.BASE_URL}/{test_config.USER_ENDPOINT}/{user_name}"
        response = requests.delete(url)
        return response

    return _delete_user

@pytest.fixture(scope="function")
def logout_user(test_config):
    """
    Fixture to provide a function for logging out a user.
    """
    def _logout_user():
        url = f"{test_config.BASE_URL}/{test_config.USER_ENDPOINT}/logout"
        response = requests.get(url)
        return response

    return _logout_user