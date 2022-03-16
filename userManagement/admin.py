from django.contrib import admin
from userManagement import models


admin.site.register(models.Gender)
admin.site.register(models.UnVerifiedUser)
admin.site.register(models.Users)
admin.site.register(models.Complaints)
