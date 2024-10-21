from django.urls import path
from . import views


app_name = 'sanais'
urlpatterns = [
    path('', views.index, name='index'),
    path('introduce/', views.introduce, name = 'introduce'),
    path('profile/', views.profile, name='profile'),
]
