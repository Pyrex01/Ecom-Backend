from django.contrib.auth.models import User
from userManagement.models import *
from datetime import date, datetime



def delete_unverified_user():
    users = UnVerifiedUser.objects.all()
    for user in users:
        if user.Generated_Date < datetime.now():
            user.delete()