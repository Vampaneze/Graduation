"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include
from django.conf.urls import url

urlpatterns = [
    url(r'^user/', include('MyUser.urls')),
    url(r'^student/', include('Student.urls')),
    url(r'^operator/', include('Operator.urls')),
    url(r'^employee/', include('Employee.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^process/', include('Process.urls')),
    url(r'', include('homepage.urls')),
]
