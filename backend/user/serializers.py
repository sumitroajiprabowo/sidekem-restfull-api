from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from core.models import UserProfile


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group()
        fields = ('id', 'name')


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('province', 'regency', 'district', 'village', 'photo')


class RegisterSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password', 'groups', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        groups_data = validated_data.pop('groups')
        user = get_user_model().objects.create_user(**validated_data)
        UserProfile.objects.create(user=user, **profile_data)
        for group_data in groups_data:
            user.groups.add(group_data)
        return user
