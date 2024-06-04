from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="home"),
    path('delete/<int:userId>', views.Delete, name="deleteUser"),
]