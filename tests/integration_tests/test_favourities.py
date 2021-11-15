from django.urls import reverse, resolve
from django.test import Client

from favourites.views import markFavourtie, FavouriteProductListView
from favourites.models import FavouriteProduct

from pytest_django.asserts import assertTemplateUsed
import pytest

CLIENT = Client()


@pytest.mark.django_db
def test_favourite_products():

    """
    First, we test if the 'favourite-products' maps to FavouriteProductListView,
    then we if the FavouriteProductListView rendered the correct template ( favourite_product.html )
    and fetched the products from the correct model ( FavouriteProduct )
    """

    # Testing if the 'favourite-products' maps to 'FavouriteProductListView'
    url = reverse('favourite-products')
    assert resolve(url).func.view_class, FavouriteProductListView

    credentials = {
        'first_name': 'Test',
        'last_name': 'User',
        'username': 'TestUser',
        'email': 'testuser@testing.com',
        'password1': 'TestPassword',
        'password2': 'TestPassword'
    }
    temp_user = CLIENT.post(reverse('signup'), credentials)
    CLIENT.post(reverse('login'), {'username': 'TestUser', 'password': 'TestPassword'})

    # Testing if FavouriteProductListView rendered the correct template ( favourite_product.html ) and
    # also testing if it fetched the products from the correct model ( FavouriteProduct )
    response = CLIENT.get(reverse('favourite-products'))
    assert response.status_code == 200
    assert FavouriteProductListView.model == FavouriteProduct 
    assertTemplateUsed(response, 'favourite_product.html')
