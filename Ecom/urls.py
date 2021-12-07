from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

from django.contrib import admin
from django.urls import path , include , re_path


schema_view = get_schema_view(
   openapi.Info(
      title="SHOPING_BAZAR API",
      default_version='v1',
      description="backend api for shoping bazar",
      contact=openapi.Contact(email="khanshafique.ahamed@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
   path('admin/', admin.site.urls),
   re_path(r"docs(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path("docs/", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path("user/",include("userManagement.urls")),
   path("store/",include("store.urls")),
   path("resident/",include("addressCollection.urls"))
]
