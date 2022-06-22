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
from django.conf.urls.static import static
from django.conf import settings
from board import views

# URLConf파일을 2개로 사용하기 위해 board.urls 를 인클루드 한다.
urlpatterns = [
    # 앱의 첫화면(원래는 로켓화면, 현재는 바로가기 링크로 수정)
    path('', views.index, name="index"),
    # 관리자 모드
    path('admin/', admin.site.urls),
    # 게시판 경로 설정
    path('board/', include('board.urls')),
]
# 첨부파일을 media폴더에 저장하기 위한 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
