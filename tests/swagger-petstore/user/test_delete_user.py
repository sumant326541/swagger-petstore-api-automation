import pytest

#@pytest.mark.skip("Skipping test_create_user for now")
def test_delete_user_by_name(create_user, delete_user, get_user):
    """
    Test case to delete a user by username using the delete_user fixture.
    """
    response = create_user()
    data = response.json()
    assert response.status_code == 200
    # Verify the user is created and can be retrieved
    get_user_response = get_user(data["username"])
    assert get_user_response.status_code == 200, "User should be created and found"
    
    # Delete the user using the delete_user fixture
    delete_response = delete_user(data["username"])
    assert delete_response.status_code == 200

    # Verify the user is deleted and cannot be retrieved
    get_user_response = get_user(data["username"])
    assert get_user_response.status_code == 404, "User should be deleted and not found"
