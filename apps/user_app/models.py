from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from datetime import date


import re

class UsersManager(models.Manager):
    def basic_validator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        PASS_REGEX = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,12}$')
        NAME_REGEX = re.compile(r"^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$")
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "Your First Name is too short!"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Your Last Name is too short!"
        if not NAME_REGEX.match(postData['first_name']):
            errors['first_name'] = "First Name Invalid Form"
        if not NAME_REGEX.match(postData['last_name']):
            errors['last_name'] = "Last Name Invalid Form"
        if len(postData['email']) < 2:
            errors['email'] = "Your Last Name is too short!" 
        if postData['password'] != postData['password_conf']:
            errors['password'] = "Your Passwords Do Not Match!"
        if Users.objects.filter(email = postData['email']):
            errors['email'] = "Email already registered!"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email is not in correct format"
        if not PASS_REGEX.match(postData['password']):
            errors['password'] = 'Password is incorrect format'
        return errors

class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length = 45)
    password = models.CharField(max_length = 70)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UsersManager()

class Businesses(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length = 45)
    user = models.ForeignKey(Users, related_name='user', on_delete=models.PROTECT)
    stock_code = models.CharField(max_length=25, default='AAPL')
    listing = models.CharField(max_length=25, default='AAPL')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class data(models.Model):
    sales = models.CharField(max_length=45)
    products = models.CharField(max_length=45)
    employees = models.CharField(max_length=45)
    business = models.ForeignKey(Businesses, related_name='business', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Retirement(models.Model):
    asset_one = models.CharField(max_length=45)
    asset_two = models.CharField(max_length=45)
    asset_three = models.CharField(max_length=45)
    asset_one_percentage = models.IntegerField()
    asset_two_percentage = models.IntegerField()
    asset_three_percentage = models.IntegerField()
    user = models.ForeignKey(Users, default=1, related_name='user_retire', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)