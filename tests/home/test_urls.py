from django.urls import reverse, resolve
from home.views import RedirectHomeView, HomeView


def test_redirect_home_url():

    """ Testing if the 'redirect_home' route maps to our 'RedirectHomeView' view """

    url = reverse('redirect_home')
    assert resolve(url).view_name == 'redirect_home'
    assert resolve(url).func, RedirectHomeView


def test_home_url():

    """ Testing if the 'home' route maps to our 'HomeView' view """

    url = reverse('home')
    assert resolve(url).view_name == 'home'
    assert resolve(url).func.view_class, HomeView