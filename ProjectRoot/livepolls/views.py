# Create your views here.

"""
단축함수 : 장고에서 웹 프로그램 개발시 자주 사용하는 기능을 내장함수로
    제공하고 있는데 이를 단축함수라 표현한다.
    대표적으로 render()와 같은 함수가 있다.
"""
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

# Model(Question테이블)을 사용하기 위한 임포트
from livepolls.models import Choice, Question

# 메인함수 : 기능은 없고 단순히 바로가기 링크만 있는 페이지로 구성
# views.py에 함수를 정의할 경우 request 내장객체는 필수로 기술해야 한다.
def main(request):
    # render()함수는 웹브라우저에 해당 템플릿의 내용을 출력하는 역할을 한다.
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


"""
get_object_or_404(모델클래스, 검색조건)
    : 모델클래스(테이블)에서 검색 조건에 맞는 객체를 조회(select)하여 반환한다.
    만약 조건에 맞는 객체가 없다면 Http404 에러를 발생시킨다.
"""


def detail(request, question_id):
    # URL패턴을 통해 전달된 일련번호로 Question 테이블을 검색한 후 반환한다.
    question = get_object_or_404(Question, pk=question_id)
    # 반환된 객체를 딕셔너리로 저장한 후 템플릿으로 전달한다.
    return render(request, "livepolls/detail.html", {"question": question})


# 투표처리 : 선택한 항목의 votes컬럼을 +1 해준다.
# 매개변수로 전달된 question_id는 URL을 통해 전달된 값이다.
def vote(request, question_id):
    # 선택한 질문의 일련번호를 통해 레코드를 얻어온다.
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST["choice"] : <form>태그를 통해 submit(전송)된 값이다. 즉 선택한 값.
        # detail페이지에서 선택한 항목을 통해 Choice테이블에서 레코드를 가져온다.
        # Question테이블과 외래키 관계에 있는 테이블에서 PK로 전달된 항목하나를 가져온다.
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # 예외가 발생하면 detail페이지를 다시 렌더링한다. 이때 에러메세지를 전달한다.
        return render(
            request,
            "livepolls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice. 투표 항목의 선택이 잘못되었습니다.",
            },
        )
    else:
        # try절의 코드가 정상적으로 실행되면 가져온 레코드를 통해 votes항목을 +1 업데이트한다.
        selected_choice.votes += 1
        # 앞에서 처리한 내용을 실제 테이블에 적용한다.
        selected_choice.save()
        # 정상 처리되면 result(결과)페이지로 이동한다.
        return HttpResponseRedirect(reverse("livepolls:results", args=(question.id,)))
        """
            reverse(url의별칭, 인수)    
                : 별칭과 인수를 통해 URL을 만들기 위한 함수이다.
                보통은 요청이 있을때 URL을 분석한 후 필요한 views를 호출하지만
                이 경우에는 별칭을 통해 거꾸로 URL을 만들기 때문에 reverse라는 이름이
                붙여졌다.
        """


def results(request, question_id):
    # 파라미터로 전달된 값에 해당하는 질문 레코드를 가져온다.
    question = get_object_or_404(Question, pk=question_id)
    # 템플릿 렌더링
    return render(request, "livepolls/results.html", {"question": question})
