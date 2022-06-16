"""DjangoApps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

"""
해당 URLconf는 프로젝트 레벨이므로 livepolls앱의 views파일(모듈)을
임포트 해야만 접근할 수 있다.
"""
from livepolls import views

"""
장고에서는 URL패턴 작성법
    path(요청URL패턴, 처리할 view의 함수명, URL의 별칭)
    위 내용은 서블릿의 매핑과 동일한 역할을 한다.
"""
urlpatterns = [
    path("admin/", admin.site.urls),
    # http://localhost:8000/ 으로 요청이 들어오면 로켓화면대신 메인화면으로 대체한다.
    path("", views.main, name="main"),  # 메인화면 추가
    # 방법 2 : 2개의 파일에 작성
    # 설문과 관련된 요청이 들어오면 뒷 부분은 앱수준의 urls.py에서 매핑을 진행한다.
    path("livepolls/", include("livepolls.urls")),
]
