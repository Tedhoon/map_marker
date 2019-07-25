"""triphub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from place_select.views import place_select ,attraction , next_select_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , place_select , name = "place_select"),
    path('attraction/', attraction , name = "attraction" ),
    path('next_select_page/', next_select_page, name = "next_select_page"),
]   
