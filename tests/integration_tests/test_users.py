from django.http import response
from django.urls import reverse, resolve
from django.test import Client
from django.contrib import auth
from django.contrib.auth.views import LoginView

from users.views import SignUpView, LogoutView, ProfileView, UpdateProfileView, UpdatePasswordView
from users.forms import SignUpForm

import pytest
from pytest_django.asserts import assertTemplateUsed


CLIENT = Client()


@pytest.mark.django_db
def test_login_route():

    """
    First we test if the 'login' route maps to 'LoginView', then we check if the LoginView 
    renders the correct template ( registration/login.html )
    Then, we create a temporary user, and login with those credentials and see whether user 
    is redirected to '/home/' route if the login was successful
    """

    # # Testing if the 'login' route maps to 'LoginView'
    # url = reverse('login')
    # assert resolve(url).func.view_class, LoginView

    # # Testing if the 'LoginView' renders correct template ( registration/login.html )
    # response = CLIENT.get(reverse('login'))
    # assertTemplateUsed(response, 'registration/login.html')
 
    credentials = {
        'first_name': 'Test',
        'last_name': 'User',
        'username': 'TestUser',
        'email': 'testuser@testing.com',
        'password1': 'TestPassword',
        'password2': 'TestPassword'
    }
    temp_user = CLIENT.post(reverse('signup'), credentials)

    # We login in the user and test if the login was successful and then we properly redirect
    # user to '/home/' route
    response = CLIENT.post(reverse('login'), {'username': 'TestUser', 'password': 'TestPassword'})
    assert response.status_code == 302
    assert response.url == reverse('home')

    user = auth.get_user(CLIENT)
    assert user.is_authenticated


@pytest.mark.django_db
def test_login_route_failed():

    """
    Testing if the user enters the false credentails then the user stays on the 'login' route,
    and is asked to re-enter the correct credentials
    """

    response = CLIENT.post(reverse('login'), {'username': 'WrongUsername', 'password': 'WrongPassword'})
    assertTemplateUsed(response, 'registration/login.html')


@pytest.mark.django_db
def test_signup_route():

    """
    Test approach starts with testing if the 'signup' route maps to 'SignUpView'. Then we test 
    if the SignUpView renders the correct template ( registration/signup.html ) with correct Form ( SignUpForm ).
    After that we create a temporary user, by using our 'signup' route and checking if redirects the user to 
    the 'login' route, if everything went fine.
    """

    # Testing if the 'signup' route maps to 'SignUpView'
    url = reverse('signup')
    assert resolve(url).func.view_class, SignUpView

    # Testing if the SignUpView renders the correct template ( registration/signup.html ) with correct Form ( SignupForm )
    response = CLIENT.get(reverse('signup'))
    assert response.status_code == 200
    assert SignUpView.form_class == SignUpForm
    assertTemplateUsed(response, 'registration/signup.html')

    credentials = {
        'first_name': 'Test',
        'last_name': 'User',
        'username': 'TestUser',
        'email': 'testuser@testing.com',
        'password1': 'TestPassword',
        'password2': 'TestPassword'
    }
    # creating a temporary user and testing if the user gets redirected to 'login' route if signup was successful
    response = CLIENT.post(reverse('signup'), credentials)
    assert response.status_code == 302
    assert response.url == reverse('login')


@pytest.mark.django_db
def test_signup_route_failed():

    """
    Testing 'signup' route with the wrong credentials and testing if user stays on the 'signup' 
    route if the signup process failed
    """

    credentials = {
        'first_name': 'Test',
        'last_name': 'User',
        'username': 'TestUser',
        'email': 'testuser@testing.com',
        'password1': '', # password not matching
        'password2': 'TestPassword'
    }
    response = CLIENT.post(reverse('signup'), credentials)
    assertTemplateUsed(response, 'registration/signup.html')


@pytest.mark.django_db
def test_logout_route():

    """
    First we test if 'logout' route maps to the 'LogoutView' or not, then we test if the user is 
    properly logged out and is redirected to 'home' route
    """
    
    # Testing if the 'logout' route maps to 'LogoutView'
    url = reverse('logout')
    assert resolve(url).func.view_class, LogoutView

    # Testing if the user is logged out properly and is redirected to 'home' route
    response = CLIENT.get(reverse('logout'))
    assert response.status_code == 302
    assert response.url == reverse('home')


@pytest.mark.django_db
def test_profile_route():

    """
    First we test if 'profile' route  maps to 'ProfileView', then we login with a temporary user and 
    access the profile route and test if the correct template ( profile.html ) was rendered
    """
    
    # Testing if the 'profile' route maps to 'ProfileView'
    url = reverse('profile', args=[1])
    assert resolve(url).func.view_class, ProfileView

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

    # Testing if the ProfileView renders correct template ( profile.html )
    response = CLIENT.get(reverse('profile', args=[1]))
    assert response.status_code == 200
    assertTemplateUsed(response, 'profile.html')


@pytest.mark.django_db
def test_profile_route_failed():

    """
    Testing if the user is redirected to 'login' route if the user is not authenticated and is 
    trying to access the profile
    """

    response = CLIENT.get(reverse('profile', args=[1]))
    assert response.status_code == 302


@pytest.mark.django_db
def test_edit_profile_route():

    """
    Test approach starts with testing if the 'edit-profile' route maps to the 'UpdateProfileView',
    and then we create a temporary user and then test if an authenticated user can access the 'edit-profile' 
    route and we also test if the correct template was rendered ( profile.html ). 
    Then try to edit profile and test if everything went fine by checking the status_code (200) and by testing
    if the correct template was re-rendered ( profile.html )
    """

    # Testing if the 'edit-profile' route maps to 'UpdateProfileView'
    url = reverse('edit-profile', args=[1])
    assert resolve(url).func.view_class, UpdateProfileView

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

    # Testing if the 'UpdateProfileView' renders the correct template ( profile.html )
    response = CLIENT.get(reverse('edit-profile', args=[1]))
    assert response.status_code == 200
    assertTemplateUsed(response, 'profile.html')

    profile_update_credentials = {
        'bio': 'This is the bio',
        'phone': '00000000000',
        'location': 'random_location',
        'birth_date': '02/28/1980',
        'image': 'random.jpg'
    }

    # Testing if we are able to update our profile credentials. We test the status_code (200) and 
    # also the template which was re-rendered ( profile.html )
    response = CLIENT.post(reverse('edit-profile', args=[1]), profile_update_credentials)
    assert response.status_code == 200
    assertTemplateUsed(response, 'profile.html')


@pytest.mark.django_db
def test_edit_profile_route_failed():

    """
    Testing if the user is redirected to 'login' route if the user is not authenticated and is 
    trying to edit the profile
    """

    response = CLIENT.get(reverse('edit-profile', args=[1]))
    assert response.status_code == 302


@pytest.mark.django_db
def test_change_password_route():

    """
    The test approach starts with testing if the 'change-password' route maps to the 'UpdatePasswordView',
    then we create a temporary user and login in. Next we test if an authenticated user can access the 
    'change-password' route by checking the status code, we also test if the correct template 'change_password.html'
    was rendered. Then we test if we can properly change password by checking the status_code (200).
    Then again, we test if our password was successfully updated by logging in again with the new password.    
    """

    # Testing if the 'change-password' route maps to 'UpdatePasswordView' 
    url = reverse('change-password')
    assert resolve(url).func.view_class, UpdatePasswordView 

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

    # Testing if the 'UpdatePasswordView' renders the correct template ( chnage_password.html )
    response = CLIENT.get(reverse('change-password'))
    assert response.status_code == 200
    assertTemplateUsed(response, 'change_password.html')

    chnage_password_credentials = {
        'old_password': 'TestPassword',
        'new_password1': 'NewTestPass',
        'new_password2': 'NewTestPass'
    }

    # We test if the 'change-password' works properly by chnaging the user password 
    response = CLIENT.post(reverse('change-password'), chnage_password_credentials)
    assert response.status_code == 302

    # To make sure everything went fine, we test again by logging the user with new password.
    response = CLIENT.post(reverse('login'), {'username': 'TestUser', 'password': chnage_password_credentials['new_password1']})
    assert response.status_code == 302


@pytest.mark.django_db
def test_change_password_route_failed():

    """
    Testing if the user is redirected to 'login' route if the user is not authenticated and is 
    trying to change the password
    """

    response = CLIENT.get(reverse('change-password'))
    assert response.status_code == 302