import pytest

#@pytest.mark.skip("Skipping test_create_user for now")
def test_logout(logout_user):
    """
    Test case for logging out a user using the logout_user fixture.
    """
    # Call the logout_user fixture to log out the user
    response = logout_user()
    # Verify the response
    assert response.status_code == 200
    # Check the response text
    assert response.text == "User logged out"
