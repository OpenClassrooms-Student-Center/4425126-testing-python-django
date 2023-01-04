from django.contrib.auth.models import User
from django.test import Client

from products.models import Product
from favourites.models import FavouriteProduct


import secrets
import pytest

@pytest.fixture
def client():
    client = Client()
    return client

@pytest.fixture
def user(client):
    credentials = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'TestUser',
            'email': 'testuser@testing.com',
            'password1': 'TestPassword',
            'password2': 'TestPassword'
        }

    user = User.objects.create(
        username = credentials['username'],
        password = credentials['password1'],
    )

    temp_user = client.post('/user/signup/', credentials)
    client.post('/user/login/', {'username': 'TestUser', 'password': 'TestPassword'})
    return user

@pytest.fixture
def product():
    product = Product.objects.create(
        name=secrets.token_hex(5),
        image=secrets.token_hex(10),
        description=secrets.token_hex(20),
        price=20.5
    )
    return product


@pytest.mark.django_db
def test_product_str(client, product):

    """
    We are creating a Product object and testing if our __str__ is properly implemented 
    """
    assert str(product) == product.name


@pytest.mark.django_db
def test_is_favourite(client, user, product):

    """
    Wr are creating a Product object, a user object and also a temporary user to pass Login Check,
    Then we are creating a FavouriteProduct object and testing if our is_favourite method is properly working
    """

    FavouriteProduct.objects.create(user=user, product=product, is_favourite=False)

    assert product.is_favourite() == False