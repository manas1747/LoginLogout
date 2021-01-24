from django.contrib import admin
from django.urls import path
from .views import index, userdetail, signup, signin, signout

urlpatterns = [
    path('', index, name="index"),
    path('userdetail/<username>', userdetail, name='userdetail'),
    path('signup', signup, name='signup'),
    path('signin', signin, name='signin'),
    path('signout', signout, name="signout"),
]
