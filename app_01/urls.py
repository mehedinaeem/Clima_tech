# app_01/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('tree_plant/', views.home, name='tree_plant'),
    path('recycle/', views.recycle, name='recycle'),
]
