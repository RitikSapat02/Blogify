
from django.urls import path
from . import views

app_name = 'App_Blog' #namespace

urlpatterns = [
   path('',views.blog_list,name='blogs'),
]
