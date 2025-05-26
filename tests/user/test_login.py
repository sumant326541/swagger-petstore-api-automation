import re
import pytest

#@pytest.mark.skip("Skipping test_create_user for now")
def test_login(create_user, user_payload,login_user):
    """
    Test case for logging in a user using the login_user fixture.
    """
    # Create a user first
    create_response = create_user()
    assert create_response.status_code == 200
    data = create_response.json()
   
    # Log in the user using the login_user fixture
    login_response = login_user(data["username"], user_payload["password"])
    assert login_response.status_code == 200
    # Verify the login response
    assert re.search(r"Logged in user session: \d+", login_response.text)
