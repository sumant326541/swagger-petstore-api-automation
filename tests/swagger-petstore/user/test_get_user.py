import pytest

#@pytest.mark.skip("Skipping test_create_user for now")
def test_get_user_by_name(create_user, get_user):
    """
    Test case to get a user by name using the get_user fixture.
    """
    response = create_user()
    data = response.json()
    assert response.status_code == 200
    # Verify the user is created and can be retrieved
    get_user_response = get_user(data["username"])
    assert get_user_response.status_code == 200, "User should be created and found"
    
    # Verify the response contains the expected user data
    assert get_user_response.json()["username"] == data["username"]
    # Verify the response matches the created user data
    assert get_user_response.json() == data
