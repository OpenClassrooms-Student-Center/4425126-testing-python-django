from django.urls import reverse, resolve
from django.test import Client

from home.views import RedirectHomeView, HomeView
from products.models import Product

from pytest_django.asserts import assertTemplateUsed
import pytest


CLIENT = Client()


@pytest.mark.django_db
def test_slash_route():

    """ 
    Our test approach starts with testing the 'redirect_home' route, whether it maps to 'RedirectHomeView'
    or not, then we test if RedirectHomeView redirected to '/home/' route. 
    Next we test if 'home' route maps to 'HomeView' and we check if the HomeView renders the 'home.html' template,
    also we check if it is rendering the data from the correct model (Product)
    """

    # Testing if the 'redirect_home' route maps to 'RedirectHomeView'
    url = reverse('redirect_home')
    assert resolve(url).func, RedirectHomeView

    # Testing if 'RedirectHomeView' redirected to '/home/' route
    response = CLIENT.get(reverse('redirect_home'))
    assert response.status_code == 302
    assert response.url == '/home/'

    # Testing if 'home' route maps to 'HomeView'
    url = reverse('home')
    assert resolve(url).func.view_class, HomeView

    # Testing if 'HomeView' renders the correct template 'home.html' and with the correct model (Product)
    response = CLIENT.get(reverse('home'))
    assert response.status_code == 200
    assertTemplateUsed(response, 'home.html')
    assert HomeView.model == Product



@pytest.mark.django_db
def test_home_route():

    """
    For this test approach, we are simply testing if 'home' route maps to 'HomeView', 
    and the 'HomeView' renders the correct template 'home.html' and with the correct model (Product)
    """

    # Testing if 'home' route maps to 'HomeView'
    url = reverse('home')
    assert resolve(url).func.view_class, HomeView

    # Testing if 'HomeView' renders the correct template 'home.html' and with the correct model (Product)
    response = CLIENT.get(reverse('home'))
    assert response.status_code == 200
    assertTemplateUsed(response, 'home.html')
    assert HomeView.model == Product
