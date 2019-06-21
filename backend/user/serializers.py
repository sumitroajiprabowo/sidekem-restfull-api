from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from core.models import UserProfile
# from areacode.serializers import ProvinceSerializer, RegencySerializer,\
#     DistrictSerializer, VillageSerializer


class GroupSerializer(serializers.ModelSerializer):
    # groups = serializers.SlugRelatedField(
    #     many=True, read_only=True, slug_field="name")

    class Meta:
        model = Group()
        fields = ('id', 'name')


class UserProfileSerializer(serializers.ModelSerializer):
    # province = ProvinceSerializer(read_only=False)
    # regency = RegencySerializer(read_only=False)
    # district = DistrictSerializer(read_only=False)
    # village = VillageSerializer(read_only=False)

    province = serializers.SerializerMethodField()
    regency = serializers.SerializerMethodField()
    district = serializers.SerializerMethodField()
    village = serializers.SerializerMethodField()

    # province = serializers.SlugRelatedField(
    #     read_only=False,
    #     slug_field='name'
    # )

    def get_province(self, obj):
        return obj.user.profile.province.name

    def get_regency(self, obj):
        return obj.user.profile.regency.name

    def get_district(self, obj):
        return obj.user.profile.district.name

    def get_village(self, obj):
        return obj.user.profile.village.name

    class Meta:
        model = UserProfile
        fields = ('province', 'regency', 'district', 'village', 'photo')


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=True)
    # groups = GroupSerializer(many=False)
    # groups = serializers.SerializerMethodField()

    # return [group.name for group in obj.groups]
    # def get_groups(self):
    #     groups = Group.objects.filter(user = request.user)

    def get_groups(self, obj):
        return obj.groups.values_list('name', flat=True)

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
