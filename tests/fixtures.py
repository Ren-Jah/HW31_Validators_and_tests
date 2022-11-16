from datetime import datetime

import pytest


@pytest.fixture
@pytest.mark.django_db
def access_token(client, django_user_model):
    username = 'testuser'
    password = 'testpassword'
    birth_date = datetime.date.today() - datetime.timedelta(days=5000)
    django_user_model.objects.create_user(
        username=username,
        password=password,
        birth_date=birth_date,
        role='admin'
    )

    response = client.post(
        "/users/token/",
        {"username": username, "password": password},
        content_type='application/json'
    )

    return response.data['access']