from django.urls import path
from . import views


app_name = 'board'
urlpatterns = [
    path('',  views.index, name='index'),
    path('<int:board_num>/', views.detail, name='detail'),
]

