# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from hashlib import sha1

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

GENDER_CHOICES = (
    ('male', 'male'),
    ('female', 'female'),
    ('Other', 'other')
)

# Create your models here.


class Company(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    is_active = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    org_name = models.CharField(max_length=100, unique=True)
    date_joined = models.DateTimeField(auto_now=True)
    logo = models.URLField()

    class Meta:
        db_table = 'company'


class Users(AbstractUser):
    objects = models.Manager()
    is_superuser = models.BooleanField(default=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    display_picture = models.URLField(default=None, null=True)
    forget_pass_code = models.CharField(max_length=40, null=True)
    forget_pass_code_validity = models.DateTimeField(null=True)

    class Meta:
        unique_together = ('email',)
        db_table = "users"


class TokenManager(models.Manager):
    def delete_session(self, *args, **kwargs):
        if "key" in kwargs:
            tokent_str = kwargs['key']
            Token.objects.filter(key=tokent_str).delete()
        return True

    def is_valid(self, *args, **kwargs):

        if "key" in kwargs:
            tokent_str = kwargs['key']
            Token.objects.filter(
                key=tokent_str, expires_at__lte=timezone.now()).delete()
            tokens = Token.objects.filter(
                key=tokent_str, expires_at__gte=timezone.now()).get()
        return tokens


class Token(models.Model):
    user = models.ForeignKey(Users)
    key = models.CharField(primary_key=True, max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=None)

    objects = TokenManager()

    class Meta:
        db_table = 'access_tokens'
        db_tablespace = 'default'

    def save(self, *args, **kwargs):
        user_id_str = self.user.id
        self.expires_at = timezone.now() + datetime.timedelta(days=30)
        exists, self.key = self.generate_key(user_id_str)
        if not exists:
            super(Token, self).save(*args, **kwargs)

        return self

    def generate_key(self, id_):
        existing_token = None
        exists = True
        tokens = Token.objects.filter(
            user_id=id_, expires_at__gte=timezone.now()).values("key")
        for token in tokens:
            existing_token = token['key']
            token = existing_token
        if existing_token is None:
            exists = False
            token = sha1(id_.__str__() + str(timezone.now())).hexdigest()
            Token.objects.filter(
                user=id_, expires_at__lte=timezone.now()).delete()
        return exists, token


class Device(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(Company)
    date_joined = models.DateTimeField(auto_now=True)
    driver_name = models.CharField(max_length=100)

    class Meta:
        unique_together = (('owner', 'name'))


class DeviceLogs(models.Model):
    AC_CHOICES = [('ON', 'ON'), ('OFF', 'OFF')]

    objects = models.Manager()

    id = models.AutoField(primary_key=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    updated_at = models.DateTimeField()
    status = models.CharField(max_length=20)
    latitude = models.FloatField()
    longitude = models.FloatField()
    speed = models.FloatField()
    altitude = models.FloatField()
    odometer = models.IntegerField()
    address = models.TextField()
    fuel_level = models.FloatField()
    temperature = models.FloatField(null=True)
    ac_status = models.CharField(max_length=3, choices=AC_CHOICES)
    fuel_diff = models.FloatField(null=True)
