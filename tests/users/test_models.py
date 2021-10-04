from django.contrib.auth.models import User
from users.models import Profile

import pytest

@pytest.mark.django_db
def test_profile_str():

    """
    Testing whether Profile's __str__ method is implemented properly
    """

    user = User.objects.create(username='TestUser', password='random_password')
    profile = Profile(user=user)

    assert str(profile) == f"Profile of {user.get_full_name()}"
