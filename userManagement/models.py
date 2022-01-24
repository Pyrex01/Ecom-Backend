from django.db import models
from django.contrib.auth.models import BaseUserManager ,AbstractBaseUser , PermissionsMixin
import uuid
import datetime

class MyUserManager(BaseUserManager):
    def create_user(self, **kwargs):
        """
        Creates and saves a User with the given name, date of
        birth and password.
        """
        if not First_Name:
            raise ValueError('Users must have an name First Name')
        user = self.model(**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, **kwargs):
        """
        Creates and saves a superuser with the given name, date of
        birth and password.
        """
        user = self.model(**kwargs)
        user.is_superuser =True
        user.is_admin = True
        user.is_staff = True
        user.set_password(kwargs["password"])
        user.save(using=self._db)
        return user


class Gender(models.Model):
    type= models.CharField(max_length=10)
    def __str__(self):
        return self.type

class Users(AbstractBaseUser,PermissionsMixin):
    First_Name = models.CharField(max_length=40,)
    Second_Name = models.CharField(max_length=40)
    Email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    Gender = models.ForeignKey(Gender,on_delete=models.SET_NULL,null=True)
    Photo = models.TextField(null=True,blank=True)
    Phone = models.CharField(max_length=13)
    objects = MyUserManager()
    USERNAME_FIELD = 'Email'
    REQUIRED_FIELDS = ['First_Name','Second_Name','Phone']
    def __str__(self):
        return self.First_Name + ":" + self.Email



class UnVerifiedUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    First_Name = models.CharField(max_length=40,)
    Second_Name = models.CharField(max_length=40)
    Email = models.EmailField()
    is_admin = models.BooleanField(default=False)
    Gender = models.ForeignKey(Gender,on_delete=models.CASCADE)
    Photo = models.TextField(null=True)
    password = models.CharField(max_length=128)
    OTP = models.CharField(max_length=6)
    Generated_Date = models.DateTimeField(auto_now_add=True)
    Phone = models.CharField(max_length=13)
        
    def __str__(self):
        return self.First_Name


class Complaints(models.Model):
    Title = models.CharField(max_length=60)
    Description = models.TextField()
    User = models.ForeignKey(Users,on_delete=models.CASCADE)