from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
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


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""
    email = serializers.CharField()
    password = serializers.CharField(
        style={
            'input_type': 'password'
        },
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            msg = _('Unable to authenticate with provide credentials')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs
