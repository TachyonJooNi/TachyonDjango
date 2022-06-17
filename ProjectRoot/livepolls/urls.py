from django.urls import path
from . import views

# app_name은 차후 URL처리를 위한 네임스페이스로 활용된다.
app_name = "livepolls"

# 네임스페이스로 처리되므로 livepolls/를 제외한 나머지 URL패턴은 기술하면 된다.
urlpatterns = [
    # 투표 목록 보기. 등록된 모든 투표 항목이 리스팅된다.
    # http://localhost:8000/livepolls
    path("", views.index, name="index"),
    #
    # 투표항목 상세보기. 질문 하위에 등록한 내용이 출력되어 투표를 진행할수 있음.
    # http://localhost:8000/livepolls/PK번호
    path("<int:question_id>/", views.detail, name="detail"),
    #
    # 투표 결과보기.
    # http://localhost:8000/livepolls/PK번호/result/
    path("<int:question_id>/results/", views.results, name="results"),
    #
    # 투표 처리하기.
    # http://localhost:8000/livepolls/PK번호/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
