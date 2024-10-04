
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('',include('app_01.urls')),
    # path('',include('app_02.urls')),
]
