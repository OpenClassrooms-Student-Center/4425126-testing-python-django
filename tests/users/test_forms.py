from django.contrib.auth.models import User

from users.forms import SignUpForm

import pytest

@pytest.fixture
def temp_user():
    user = {
        'username': 'TestUser',
        'password1': 'test-password',
        'password2': 'test-password',
        'email': 'testuser@testing.com',
        'first_name': 'Test',
        'last_name': 'User'
    }
    return user



@pytest.mark.django_db
def test_signup_form_validate(temp_user):

    """
    Testing the SignUpForm to check if the user input data is properly validated or not
    """
    user = SignUpForm(data=temp_user)    

    assert user.is_valid()


@pytest.mark.django_db
def test_signup_form_save_method(temp_user):

    """
    Testing if the User object is created properly by using SignUpForm or not
    """
    form = SignUpForm(data=temp_user)
    user = form.save()

    assert isinstance(user, User)