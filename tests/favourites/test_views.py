from django.test import Client
from django.urls import reverse, resolve

import pytest
from pytest_django.asserts import assertTemplateUsed

@pytest.fixture
def client():
    client = Client()
    return client

@pytest.fixture
def login_user(client):
    credentials = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'TestUser',
            'email': 'testuser@testing.com',
            'password1': 'TestPassword',
            'password2': 'TestPassword'
        }
    temp_user = client.post('/user/signup/', credentials)
    client.post('/user/login/', {'username': 'TestUser', 'password': 'TestPassword'})
    return temp_user


@pytest.mark.django_db
def test_FavouriteProductListView(client, login_user):

    """
    Testing if FavouriteProductListView is properly rendered with 200 status code and in second assert,
    we are making sure it returns the correct template 'favourite_product.html'
    """
    response = client.get(reverse('favourite-products'))
    
    assert response.status_code == 200
    assertTemplateUsed(response, 'favourite_product.html')
