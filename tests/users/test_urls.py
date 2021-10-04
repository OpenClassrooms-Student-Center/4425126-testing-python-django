from django.urls import reverse, resolve
from django.contrib.auth.views import LoginView

from users.views import SignUpView, LogoutView, ProfileView, UpdateProfileView, UpdatePasswordView


def test_login_url():

    """
    Testing if the 'login' route maps to LoginView
    """

    url = reverse('login')
    assert resolve(url).view_name == 'login'
    assert resolve(url).func.view_class, LoginView


def test_signup_url():

    """
    Testing if the 'signup' route maps to SignUpView
    """

    url = reverse('signup')
    assert resolve(url).view_name == 'signup'
    assert resolve(url).func.view_class, SignUpView


def test_logout_url():

    """
    Testing if the 'logout' route maps to LogoutView
    """

    url = reverse('logout')
    assert resolve(url).view_name == 'logout'
    assert resolve(url).func.view_class, LogoutView


def test_profile_url():

    """
    Testing if the 'profile' route maps to ProfileView
    """

    url = reverse('profile', args=[1])
    assert resolve(url).view_name == 'profile'
    assert resolve(url).func.view_class, ProfileView


def test_update_profile_url():

    """
    Testing if the 'edit-profile' route maps to UpdateProfileView
    """

    url = reverse('edit-profile', args=[1])
    assert resolve(url).view_name == 'edit-profile'
    assert resolve(url).func.view_class, UpdateProfileView


def test_change_password_url():

    """
    Testing if the 'change-password' route maps to UpdatePasswordView
    """

    url = reverse('change-password')
    assert resolve(url).view_name == 'change-password'
    assert resolve(url).func.view_class, UpdatePasswordView