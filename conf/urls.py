from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('configapp.urls')),  # configapp URL larini asosiy root ga uladik
]