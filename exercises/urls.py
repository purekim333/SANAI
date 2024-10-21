from django.urls import path
from . import views

app_name = 'exercises'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:exercise_pk>/delete/', views.delete, name='delete'),
    path('<int:exercise_pk>/update/', views.update, name='update'),
    path('<int:exercise_pk>/detail/', views.detail, name='detail'),
    path('<int:exercise_pk>/participate/', views.participate, name='participate'),
]
