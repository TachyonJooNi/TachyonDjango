# Create your views here.

"""
단축함수 : 장고에서 웹 프로그램 개발시 자주 사용하는 기능을 내장함수로
    제공하고 있는데 이를 단축함수라 표현한다.
    대표적으로 render()와 같은 함수가 있다.
"""
from django.shortcuts import render

# Model(Question테이블)을 사용하기 위한 임포트
from livepolls.models import Question

# 메인함수 : 기능은 없고 단순히 바로가기 링크만 있는 페이지로 구성
# views.py에 함수를 정의할 경우 request 내장객체는 필수로 기술해야 한다.
def main(request):
    # render()함수는 웹브라우저에 해당 템플릿의 내용을 출력하는 역할을 한다.+
    # 템플릿으로 전달하는 데이터가 없는 상태로 반환한다.
    return render(request, "livepolls/main.html")


# 투표앱의 첫번째 화면으로 질문이 리스팅된다.
def index(request):
    # Question 테이블에서 pub_date를 내림차순으로 정렬하여 최근 게시물 5개를 가져온다.
    latest_question_list = Question.objects.all().order_by("-pub_date")[:5]
    # 템플릿으로 데이터를 전달하기 위해 딕셔너리에 저장한다. (JDBC에서 리퀘스트 영역에 저장하듯이)
    context = {"latest_question_list": latest_question_list}
    # render함수를 통해 템플릿을 로드하면서 데이터를 전달한다.
    # 즉, 서블릿에서 데이터를 request영역에 저장한 후 forward하는것과 동일하다.
    return render(request, "livepolls/index.html", context)
