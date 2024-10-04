
from django.urls import path
from . import views

urlpatterns = [
    path('tree_plant/',views.home),
]
