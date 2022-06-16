from django.urls import path
from . import views

# app_name은 차후 URL처리를 위한 네임스페이스로 활용된다.
app_name = "livepolls"

# 네임스페이스로 처리되므로 livepolls/를 제외한 나머지 URL패턴은 기술하면 된다.
urlpatterns = [
    # http://localhost:8000/livepolls
    path("", views.index, name="index"),
    # http://localhost:8000/livepolls/PK번호
    # path("<int:question_id>/", views.detail, name="detail"),
    # http://localhost:8000/livepolls/PK번호/result/
    # path("<int:question_id>/results", views.results, name="results"),
    # http://localhost:8000/livepolls/PK번호/vote/
    # path("<int:question_id>/vote", views.vote, name="vote"),
]
