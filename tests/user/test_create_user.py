import pytest

#@pytest.mark.skip("Skipping test_create_user for now")
def test_create_user(create_user, user_payload):
    """
    Test case for creating a user using the create_user fixture.
    """
    response = create_user()
    data = response.json()
    assert response.status_code == 200
    assert data["username"] == user_payload["username"]
    assert data == user_payload
    print(f"User created with data: {data}")
