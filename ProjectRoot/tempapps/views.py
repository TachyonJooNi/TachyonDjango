# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from requests import request

from tempapps.forms import QuestionForm, WriteForm

# 템플릿 앱의 첫 화면 : 바로가기 링크가 출력된다.
def index(request):
    return render(request, "index.html")


# 템플릿 필터 사용
def templateFilter(request):
    # 정수형 변수
    num1 = 1
    num2 = 10

    # 문자형 변수
    engStr = "nakja's MustHave\r\njava <b>web</b>programming"
    hanStr = "낙자쌤의 자바 웹 프로그래밍"

    # 컬렉션형 변수(딕셔너리, 리스트)
    dictVar = {"a": "유비", "b": "관우", "c": "장비"}
    listVar = ["손오공", "저팔계", "사오정"]

    # 템플릿으로 전달한 변수를 딕셔너리로 정의
    context = {
        "num1": num1,
        "num2": num2,
        "engStr": engStr,
        "hanStr": hanStr,
        "dictVar": dictVar,
        "listVar": listVar,
    }

    # 템플릿 렌더링
    return render(request, "template_filter.html", context)


def templateTag(request):

    # 딕셔너리를 원소로 가진 리스트 정의
    books = [
        {"name": "자바", "price": 1000},
        {"name": "HTML", "price": 2000},
        {"name": "JSP", "price": 3000},
    ]
    # 값이 없는 빈 리스트
    hobbys = []
    favorites = ["운동", "공부", "여행", "경제"]
    iVar = range(1, 11)

    # 템플릿으로 전달한 데이터를 담은 딕셔너리
    context = {"books": books, "hobbys": hobbys, "favorites": favorites, "iVar": iVar}
    return render(request, "template_tag.html", context)

# 장고의 폼 생성기능 사용하기
def formCreate(request):
    '''
    Servlet의 doGet(), doPost()와 같이 하나의 함수에서 폼 출력된 전송된 값의 처리를
    동시에 하도록 권장하고 있다. 즉, POST인 경우라면 폼값을 입력한 후 전송할때의 처리를
    말한다.
    '''
    if request.method == "POST":
        # 전송방식이 POST라면 submit된 폼값을 처리한다.
        form = QuestionForm(request.POST)
        # 폼값의 유효성 빈값 검증을 한다.
        if form.is_valid():
            # 폼 데이터가 유효하면 클린데이터를 복사한다.
            user_id = form.cleaned_data['user_id']
            '''
            user_id 외에 title, content 도 동일한 방식으로 저장할 수 있다.
            여기서는 user_id만 기술했다.
            '''
            
            # 폼 데이터에 문제가 없다면 일반적으로 DB에 처리하는등의 비즈니스로직을 수행한다.

            # Views에서 페이지 이동시 사용한다.
            return HttpResponseRedirect("/tempapps/thanks/")
            # 페이지 이동이 아니라 템플릿을 렌더링하려면 아래와 같이 할수 있다. 그리고
            # 데이터를 전달할 수 있다.
            # return render(request, 'thanks.html', {'user_id':user_id})
        
        
    else:
        # 만약 GET이라면 입력폼으로 진입한다.
        form = QuestionForm()
    # 입력폼 진입을 위해 템플릿을 렌더링한다. 이때 form(폼생성기능)을 데이터로 전달한다.
    return render(request, "form_create.html", {"form": form})


def thanks(request):
    return render(request, "thanks.html")

# 글쓰기 폼 만들기 실습
def boardWrite(request):
    # 폼 클래스 객체 생성
    form = WriteForm()
    # 랜더링시 데이터로 전달하여 화면에 출력
    return render(request, "boardWrite.html", {"form": form})
    
    
    
'''
내가한거
def boardWrite(request):
if request.method == "POST":
    form = WriteForm(request.POST)
    if form.is_valid():
        user_id = form.cleaned_data['user_id']
        return render(request, 'thanks.html', {'user_id':user_id})
        # return HttpResponseRedirect("/tempapps/thanks/")
else:
    form = WriteForm()
return render(request, "boardWrite.html", {"form": form})
'''