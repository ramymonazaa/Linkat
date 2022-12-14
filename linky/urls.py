"""linky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from app1 import views
from django.conf import settings
from django.conf.urls.static import static
from . import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),
    path('home',views.home , name='home'), 
    path('search',views.search , name='search'), 
    path('register/',v.register,name='register'),
    path('register/login',v.loginPage,name='login'),
    path('logout/',v.logoutPage,name='logout'),
    path('visit_action <str:name1>',views.visit_action,name='visit_action'), 

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=staticfiles_urlpatterns()