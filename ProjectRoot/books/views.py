# Create your views here.
from django.shortcuts import render
# 클래스형 제네릭뷰를 사용하기 위한 임포트
# 템플릿뷰
from django.views.generic.base import TemplateView
# 리스트뷰
from django.views.generic import ListView
# 디테일뷰
from django.views.generic import DetailView
# 레코드 조회를 위한 모델 클래스 임포트
from books.models import Book, Author, Publisher

# books 애플리케이션 첫 화면을 출력 : TemplateView를 상속하여 정의한다.
class BooksModelView(TemplateView):
    '''
    TemplateView를 사용하는 경우 해당 클래스변수를 오버라이딩 해야한다.
    템플릿의 파일경로를 지정한다.
    클래스형 뷰를 사용하는 경우 함수형 뷰 처럼 render()함수를 통해 반환하지 않아도
    자동으로 랜더링 처리된다.
    '''
    template_name = 'books/index.html'

    # 템플릿으로 전달할 데이터가 있는경우 해당 함수를 오버라이딩 한다.
    def get_context_data(self, **kwargs):
        # 오버라이딩 하는 경우 반드시 super()를 통해 첫줄에 선언해야 한다.
        context = super().get_context_data(**kwargs)
        # 템플릿으로 전달한 데이터를 List형식으로 저장한다.
        context['model_list'] = ['Book', 'Author', 'Publisher']
        # return도 필수적으로 필요하다.
        return context