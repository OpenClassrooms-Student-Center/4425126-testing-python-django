from django.contrib.auth.models import User

from users.forms import SignUpForm

import pytest

class TestUsersForms:
    temp_user = {
            'username': 'TestUser',
            'password1': 'test-password',
            'password2': 'test-password',
            'email': 'testuser@testing.com',
            'first_name': 'Test',
            'last_name': 'User'
        }

    @pytest.mark.django_db
    def test_signup_form_validate(self):
        """
        Testing the SignUpForm to check if the user input data is properly validated or not
        """
        user = SignUpForm(data=self.temp_user)    

        assert user.is_valid()


    @pytest.mark.django_db
    def test_signup_form_save_method(self):
        """
        Testing if the User object is created properly by using SignUpForm or not
        """

        form = SignUpForm(data=self.temp_user)
        user = form.save()

        assert isinstance(user, User)