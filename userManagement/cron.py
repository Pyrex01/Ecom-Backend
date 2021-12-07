from django.contrib.auth.models import User
from userManagement.models import *
from datetime import time, timezone, datetime
import pytz

UTC = pytz.UTC

def delete_unverified_user():
    users = UnVerifiedUser.objects.all()
    print("|cronjob| delete unvierified users fired")
    for user in users:
        print("user date",type(user.Generated_Date.utcnow()) , "systyem",type(datetime.now().utcnow()))
        print("user data", user.Generated_Date.utcnow())
        print("now date", datetime.now().utcnow())
        
        if (user.Generated_Date.utcnow() + datetime(minute=3).utcnow()) < datetime.now().utcnow() :
            user.delete()