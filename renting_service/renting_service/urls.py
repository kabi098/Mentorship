# renting_service/urls.py

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render # <--- ADD THIS IMPORT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('users.urls')),
    # This line will now work perfectly!
    path('', lambda request: render(request, 'home.html'), name='home'),
]