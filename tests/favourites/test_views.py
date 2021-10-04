from django.test import Client
from django.urls import reverse, resolve

import pytest
from pytest_django.asserts import assertTemplateUsed

client = Client()


@pytest.mark.django_db
def test_FavouriteProductListView():

    """
    Testing if FavouriteProductListView is properly rendered with 200 status code and in second assert,
    we are making sure it returns the correct template 'favourite_product.html'
    """

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

    response = client.get(reverse('favourite-products'))
    
    print(response)
    assert response.status_code == 200
    assertTemplateUsed(response, 'favourite_product.html')
