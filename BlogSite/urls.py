from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include("home.urls")),
    path('user/', include("user.urls")),
    path('admin/', admin.site.urls),
]
