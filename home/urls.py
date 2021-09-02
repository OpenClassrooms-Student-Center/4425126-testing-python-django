from django.urls import path

from .views import HomeView, RedirectHomeView


urlpatterns = [
    path('', RedirectHomeView, name='redirect_home'),
    path('home/', HomeView.as_view(), name='home'),
]
