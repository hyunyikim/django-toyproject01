from django.urls import path
from . import views


'''
url 설계
* 게시글 전체조회 : / (get)
* 상세조회 : /board/5/ (get)
* 작성 페이지 : /board/new/ (get)
* 작성 : /board/new/ (post)
* 수정 페이지 :  /board/5/update/ (get)
* 수정 : /board/5/update/ (post)
* 삭제 : /board/5/delete/ (get)
'''

app_name = 'board'
urlpatterns = [
    path('',  views.index, name='index'),
    path('<int:num>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('<int:num>/update/', views.new, name='update'),
    path('<int:num>/delete/', views.delete, name='delete'),
]

