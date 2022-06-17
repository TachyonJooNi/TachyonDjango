from django.urls import path
from . import views

# 네임스페이스 정의
app_name = "tempapps"

urlpatterns = [
    # 템플릿 앱의 첫번째 화면
    path("", views.index, name="index"),
    #
    # 템플릿 필터
    path("template.filter/", views.templateFilter, name="my_filter"),
    #
    # 템플릿 태그
    path("template.tag/", views.templateTag, name="my_tag"),
    #
    # 폼 사용하기
    # path("form.create/", views.formCreate, name="formCreate"),
    #
    # path("thanks/", views.thanks),
]
