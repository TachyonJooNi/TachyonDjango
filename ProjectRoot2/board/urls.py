from django.urls import path
from . import views

# 게시판 앱의 네임스페이스
app_name = 'board'

'''
http://localhost:8000/board/
http://localhost:8000/board/list 
=> 해당 패턴들로 요청이 들어오면 게시판의 리스트(목록)를 출력한다.
    
함수형 view를 사용하기 위한 URL매핑
'''
urlpatterns = [
    path('', views.list, name="list"),
    path('list/', views.list, name="list"),
    path('view/<int:pk>/', views.view, name="view"),
    path('write/', views.write, name="write"),
    path('edit/<int:pk>/', views.edit, name="edit"),
    path('delete/<int:pk>/', views.delete, name="delete"),
]
