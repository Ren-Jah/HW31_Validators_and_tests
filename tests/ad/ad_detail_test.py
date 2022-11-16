import pytest

from ads.serializers import AdSerializer


@pytest.mark.django_db
def test_ads_detail(client, ad, access_token):

    response = client.get(f"/ad/{ad.pk}/", HTTP_AUTHORIZATION="Bearer" + access_token)
    assert response.status_code == 200
    assert response.data == AdSerializer(ad).data
