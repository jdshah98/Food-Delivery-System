from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_views
from django.conf import settings

app = settings.APP_NAME

urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html',
        redirect_authenticated_user=True,
        extra_context={'title': 'login', 'app': app})
         , name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='users/logout.html',
        extra_context={'title': 'logout', 'app': app})
         , name='logout'),
]
