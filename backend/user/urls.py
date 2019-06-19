from django.urls import include, path

from rest_framework import routers
from user.views import GroupViewSet
from . import views


router = routers.DefaultRouter()
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.CreateTokenView.as_view(), name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),

]
