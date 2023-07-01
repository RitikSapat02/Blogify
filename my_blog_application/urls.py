
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('authentication/',include('Authentication.urls')),
    path('blogs/',include('App_Blog.urls')),
]
