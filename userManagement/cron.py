from django.contrib.auth.models import User
from userManagement.models import *
from datetime import datetime ,timedelta
import pytz

UTC = pytz.UTC

def delete_unverified_user():
    users = UnVerifiedUser.objects.all()
    print("|cronjob| delete unvierified users fired")
    for user in users:
        expression = user.Generated_Date.utcnow() < datetime.datetime.now().utcnow()-datetime.timedelta(minutes=3)
        print(expression)
        if expression :
            user.delete()