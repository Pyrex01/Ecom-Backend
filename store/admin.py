from django.contrib import admin
from store import models

admin.site.register(models.Belongs)
admin.site.register(models.Categorie)
admin.site.register(models.Items)
admin.site.register(models.Orders)
admin.site.register(models.CompletedOrders)
admin.site.register(models.Return_Items)
admin.site.register(models.Completed_Return_Items)
admin.site.register(models.Cart)
admin.site.register(models.Wish_List)