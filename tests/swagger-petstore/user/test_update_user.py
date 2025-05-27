import pytest

#@pytest.mark.skip(reason="Skipping test_update_user for now")
def test_update_user(create_user, user_payload, update_user,get_user):
    """
    Test case for updating a user using the update_user fixture.
    """

    # Create a user first
    response = create_user()
    assert response.status_code == 200, "User creation failed"
    data = response.json()

    # Modify the first and last name in the user payload
    user_payload["firstName"] = "NewFirst"
    user_payload["lastName"] = "NewLast"

    # create_user returns the username
    user_Name = data["username"]

    # Update the user with the updated payload
    response = update_user(user_Name, user_payload)
    assert response.status_code == 200

    #verify the update
    verify_response = get_user(user_Name)
    assert verify_response.status_code == 200
    user_data = verify_response.json()
    assert user_data["firstName"] == "NewFirst", "First name update failed"
    assert user_data["lastName"] == "NewLast", "Last name update failed"
  