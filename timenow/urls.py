"""timenow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls), # Django Admin Panel
    path('times/', include('times.urls')), # Zeitbuchungs/-management App
    path('absence/', include('absence.urls')), # Urlaubsmanagement App
    path('', views.index, name='index'), # Default Page ohne Anmeldung
    path('', include('django.contrib.auth.urls')) # Django Authentication Library
]

handler400 = 'timenow.views.error400'
handler403 = 'timenow.views.error403'
handler404 = 'timenow.views.error404'
handler500 = 'timenow.views.error500'
