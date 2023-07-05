

from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [
    path('sign_up/', views.sign_up, name='signup'),
    path('sign_in/', views.sign_in, name='signin'),
    path('logout/', views.logout_user, name='logout'),

]
