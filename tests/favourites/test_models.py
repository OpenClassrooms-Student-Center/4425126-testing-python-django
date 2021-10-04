from django.contrib.auth.models import User

from favourites.models import FavouriteProduct
from products.models import Product

import secrets
import pytest


@pytest.mark.django_db
def test_favourite_product():

    """
    Testing if FavouriteProduct's __str__ method is properly implemented
    """

    product = Product.objects.create(
        name=secrets.token_hex(5),
        image=secrets.token_hex(10),
        description=secrets.token_hex(20),
        price=20.5
    )
    user = User.objects.create(
        username=secrets.token_hex(10),
        password=secrets.token_hex(10)
    )
    favProd = FavouriteProduct.objects.create(product=product, user=user)

    assert str(favProd) == f"product {product.name} marked favourite by {user.get_full_name()}"