"""mysite URL Configuration

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
from personal.views import (field_registration,)
from django.contrib import admin
from django.urls import path
from personal.views import (user_registration,sensor_registration,irrigation_registration)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', user_registration),
    path('plot/',field_registration),
    path('sensor/',sensor_registration),
    path('irrigation/',irrigation_registration),

]
