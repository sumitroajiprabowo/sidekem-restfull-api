from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,\
    PermissionsMixin
from django.conf import settings

from areacode.models import Province, Regency, District, Village


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Create and save a new user"""
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user"""
    email = models.EmailField(max_length=225, unique=True)
    username = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return "{}".format(self.email)


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='profile')
    province = models.ForeignKey(
        Province, on_delete=models.CASCADE,
        related_name='profile_province', null=True)
    regency = models.ForeignKey(
        Regency, on_delete=models.CASCADE,
        related_name='profile_regency', null=True)
    district = models.ForeignKey(
        District, on_delete=models.CASCADE,
        related_name='profile_district', null=True)
    village = models.ForeignKey(
        Village, on_delete=models.CASCADE,
        related_name='profile_village', null=True)
    photo = models.ImageField(upload_to='uploads', blank=True)

