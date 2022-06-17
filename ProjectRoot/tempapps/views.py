# Create your views here.
from django.shortcuts import render

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
