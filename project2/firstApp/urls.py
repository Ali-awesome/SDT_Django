from django.urls import path
# from firstApp.views import home
# from firstApp.views import views
from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.htmlhome),
]