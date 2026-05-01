"""
URL configuration for busbooking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("search_bus/", views.search_bus, name="search_bus"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path('getbus/', views.getbus, name='getbus'),
    path('book/<int:bus_id>/', views.book_bus, name='book_bus'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('designer/', views.designer, name='designer'),
    path('services/', views.services, name='services'),
    path('ajax/load-districts/', views.load_districts, name='ajax_load_districts'),
    path('ajax/load-sectors/', views.load_sectors, name='ajax_load_sectors'),
    path('ajax/load-cells/', views.load_cells, name='ajax_load_cells'),
    path('ajax/load-villages/', views.load_villages, name='ajax_load_villages'),

    
    
]
