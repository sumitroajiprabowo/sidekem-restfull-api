from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import Group

from core.models import User
from user.serializers import RegisterSerializer, GroupSerializer
# Also add these imports
from user.permissions import IsLoggedInUserOrAdmin, IsAdminUser


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
