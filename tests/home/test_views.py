from django.urls import reverse 
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
import pytest

from home.views import RedirectHomeView, HomeView


def test_RedirectHomeView():
    client = Client()
    response = client.get(reverse('redirect_home'))

    """ 
    Testing if our RedirectHomeView redirects succuessfully (status_code 302)
    For the second assert, We are testing if we redirect to the '/home/' url
     """

    assert response.status_code == 302
    assert response.url == '/home/'

@pytest.mark.django_db
def test_HomeView():
    client = Client()
    response = client.get(reverse('home'))

    """ 
    In the first assert, We are testing if our get request returns 200 (OK) status code 
    For the second assert, we are making sure that our view returns the home.html template
    """
    
    assert response.status_code == 200
    assertTemplateUsed(response, 'home.html')