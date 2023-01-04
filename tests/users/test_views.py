from django.test import Client
from django.urls import reverse, resolve

import pytest
from pytest_django.asserts import assertTemplateUsed


@pytest.fixture
def client():
    client = Client()
    return client

@pytest.fixture
def credentials():
    credentials = {
        'first_name': 'Test',
        'last_name': 'User',
        'username': 'TestUser',
        'email': 'testuser@testing.com',
        'password1': 'TestPassword',
        'password2': 'TestPassword'
    }
    return credentials

@pytest.fixture
def login(credentials, client):
    temp_user = client.post('/user/signup/', credentials)
    client.post('/user/login/', {'username': 'TestUser', 'password': 'TestPassword'})
    return temp_user

@pytest.mark.django_db
def test_UpdatePassword(login, client):

    """
    In the first assert, we are testing if there is no issue rendering template by checking 200 status code,
    For the second assert, we are checking if our view is returning 'change_password.html' template
    """
    response = client.get(reverse('change-password'))

    assert response.status_code == 200
    assertTemplateUsed(response, 'change_password.html')



@pytest.mark.django_db
def test_SignUpView(client, credentials):

    """
    In the first assert, we are checing if a user is created successfully then, the user is redirected to '/login/' route,
    For the second assert, we are checking the 302 status code(redirect)
    """
    response = client.post('/user/signup/', credentials)

    assert response.url == '/user/login/'
    assert response.status_code == 302


@pytest.mark.django_db
def test_LogoutView(client):

    """
    Testing if our LogoutView properly logouts user, In the first assert, we are checking if user is redirected to 
    home route, for the second assert we are checking 302 redirect status code
    """

    response = client.get(reverse('logout'))

    assert response.url == '/home/'
    assert response.status_code == 302


@pytest.mark.django_db
def test_ProfileView(login, client):

    """
    Testing if ProfileView is rendered properly by checking 200 status code,
    For the second assert, we are making sure that 'profile.html' template is rendered
    """
    response = client.get(reverse('profile', args=[1]))
    

    assert response.status_code == 200
    assertTemplateUsed(response, 'profile.html')


@pytest.mark.django_db
def test_Update_Profile_View(login, client):
    
    """
    Checking if our 'UpdateProfileView' returns the 'profile.html' template to show update form,
    for the second assert, we are making sure everything went fine by checking 200 status code
    """
    response = client.get(f'/user/profile/1/edit')

    assertTemplateUsed(response, 'profile.html')
    assert response.status_code == 200


