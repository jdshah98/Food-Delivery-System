from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as rest_views
from django.conf import settings
from django.conf.urls.static import static

app = settings.APP_NAME

urlpatterns = [
    path('restaurant/', rest_views.home, name='rest-home'),
    path('restaurant/about/', rest_views.about, name='rest-about'),
    path('restaurant/register/', rest_views.register, name='rest-register'),
    path('restaurant/login/', auth_views.LoginView.as_view(
        template_name='restaurants/login.html',
        redirect_authenticated_user=True,
        extra_context={'title': 'login', 'app': app})
         , name='rest-login'),
    path('restaurant/logout/', auth_views.LogoutView.as_view(
        template_name='restaurants/logout.html',
        extra_context={'title': 'logout', 'app': app})
         , name='rest-logout'),
    path('restaurant/profile/', rest_views.profile, name='rest-profile'),
    path('restaurant/add/', rest_views.FoodCreateView.as_view(
        extra_context={'title': 'Add Food', 'app': app}), name='rest-add'),
    path('restaurant/foods/<int:pk>/', rest_views.FoodDetailView.as_view(), name='rest-detail'),
    path('restaurant/list/', rest_views.FoodListView.as_view(), name='rest-list'),
    path('restaurant/delete/', rest_views.FoodDeleteView.as_view(), name='rest-delete'),
    path('restaurant/update/', rest_views.FoodUpdateView.as_view(), name='rest-update'),
    path('restaurant/order/', rest_views.FoodListView.as_view(), name='rest-order'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
