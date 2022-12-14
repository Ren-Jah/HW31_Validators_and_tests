import pytest


@pytest.mark.django_db
def test_ad_create(client, user, category, access_token):
    data = {
        "author": user.pk,
        "category": category.pk,
        "name": "Test name Ad 10 letters",
        "price": 42,
        "description": "",
        "image": None,
        "is_published": False

    }

    expected_data = {
        "id": 1,
        "is_published": False,
        "name": "Test name Ad 10 letters",
        "price": 42,
        "description": "",
        "image": None,
        "author": 1,
        "category": 1
    }

    response = client.post(
        "/ad/",
        data,
        content_type="application/json",
        HTTP_AUTHORIZATION="Bearer " + access_token)

    assert response.status_code == 201
    assert response.data == expected_data
