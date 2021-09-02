from django.urls import path
from django.contrib.auth.views import LoginView
from .views import SignUpView, LogoutView, ProfileView, UpdateProfileView, UpdatePasswordView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/edit', UpdateProfileView.as_view(), name='edit-profile'),
    path('change-password/', UpdatePasswordView.as_view(), name="change-password"),
]
