from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as rest_views
from django.conf import settings

app = settings.APP_NAME

urlpatterns = [
    path('', rest_views.home, name='rest-home'),
    path('about/', rest_views.about, name='rest-about'),
    path('register/', rest_views.register, name='rest-register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='restaurants/login.html',
        redirect_authenticated_user=True,
        extra_context={'title': 'login', 'app': app})
         , name='rest-login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='restaurants/logout.html',
        extra_context={'title': 'logout', 'app': app})
         , name='rest-logout'),
    path('profile/', rest_views.profile, name='rest-profile'),
    path('add/', rest_views.food_create, name='rest-add'),
]
