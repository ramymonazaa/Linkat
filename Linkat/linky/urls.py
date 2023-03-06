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
    path('register/register',v.register,name='register'),
    path('register/login',v.loginPage,name='login'),
    path('register/',v.register,name='register'),
    path('logout/',v.logoutPage,name='logout'),
    path('forget_password/',v.Forget_password,name='forget_password'),
    path('',v.test,name='test'),
    path('profile',views.profile,name='profile'),
    path('add_article',views.Add_article, name='add_article'),
    path('add_article',views.Add_article, name='add_article'),
    path('visit_action <str:name1>',views.visit_action,name='visit_action'), 
    path('delete_item <str:name>',views.Delete_item,name='delete_item'), 
    path('view_item <str:search>',views.View_item,name='view_item'), 
    path('add_fav <str:name1>',views.Add_fav,name='add_fav'), 
    path('change_section <str:name1>',views.Change_section,name='change_section'), 
    path('register/choose_section <str:name1>',v.Choose_section,name='choose_section'), 
    path('add_fave',views.Add_fave,name='add_fave'), 
    # path('send',views.Send,name='send'), 
    path('del_fav <str:name1>',views.Del_fav,name='del_fav'), 
    path('profile/update_user_info',views.Update_user_info,name='update_user_info'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=staticfiles_urlpatterns()