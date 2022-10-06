from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    path('',views.home,name='Products'),
    path('profile/',views.profile,name='profile'),
]
urlpatterns+=staticfiles_urlpatterns() 