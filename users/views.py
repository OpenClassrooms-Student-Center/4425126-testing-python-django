from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, View, DetailView, UpdateView

from .forms import ProfileForm, SignUpForm
from .models import Profile

@method_decorator(login_required, name='dispatch')
class UpdatePasswordView(PasswordChangeView):
    '''
    Updates password of an user

    Form parameters:
        old_password (password): old password of an user
        new_password1 (password): new password of an user
        new_password2 (password): confirm new password of an user
    '''
    form_class = PasswordChangeForm
    success_url = '/home/'
    template_name = 'change_password.html'


class SignUpView(CreateView):
    '''
    User registration

    Form parameters:
        first_name (string): first name of an user
        last_name (string): last name of an user
        username (string): username of an user
        email (email): email of an user
        password1 (password): new password of an user
        password2 (password): confirm new password of an user
    '''
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class LogoutView(View):
    '''
    Logout user
    '''
    def get(self, request):
        logout(request)
        return redirect('home')

@method_decorator(login_required, name='dispatch')
class ProfileView(DetailView):
    '''
    Fetch profile of an user if exist

    Parameters:
        pk (int): pk of an user
    Returns:
        profile of an user
    '''
    template_name = 'profile.html'
    model = Profile

@method_decorator(login_required, name='dispatch')
class UpdateProfileView(UpdateView):
    '''
    Update profile of an user if exist

    Parameters:
        pk (int): pk of an user

    Form parameters:
        user (int): id of an user
        phone (phonenumber): phonenumber of an user with country code
        bio (string): bio of an user
        location (string): location of an user
        birth_date (date): dob of an user
        image (image): profile picture of an user
    '''
    model = Profile
    form_class = ProfileForm
    template_name = 'profile.html'
    success_url = "/"
