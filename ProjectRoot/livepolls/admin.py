# Register your models here.
from django.contrib import admin

"""
    형식] 앱의이름.models.py import 클래스명
        두개 이상의 클래스가 필요하면 컴마(,)로 구분하면 된다.
        해당 모듈은 model이므로 각 클래스명은 테이블을 의미한다.
"""
from livepolls.models import Question, Choice

# 1. 관리자모드에서 출력되는 필드 순서 변경하기 : 테이블에 적용되진 않고,
# 관리자모드에서만 순서가 변경된다. 생성한 클래스는 아래 register에 추가한다.
"""
class QuestionChanger(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]
"""

# 2.필드 분리해서 보여주기 + 순서변경
"""
class QuestionChanger(admin.ModelAdmin):
    # 각 항목을 블럭으로 구분해서 제목과 입력부분을 출력한다.
    fieldsets = [
        ("질문을 입력하세요", {"fields": ["question_text"]}),
        ("날짜를 입력하세요", {"fields": ["pub_date"]}),
    ]
"""


# 3.필드접기 : 'classes': ['collapse'] 항목을 추가한다. 접기/펴기를 토글할수있다.
"""
class QuestionChanger(admin.ModelAdmin):
    fieldsets = [
        ("질문을 입력하세요", {"fields": ["question_text"]}),
        ("날짜를 입력하세요", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
"""

# 4.외래키 관계의 테이블을 한 화명에서 편집하기
# class ChoiceInline(admin.StackedInline): # 세로형으로 항목 배치
class ChoiceInline(admin.TabularInline):  # 테이블형으로 배치
    # 외래키 관계의 테이블 선택
    model = Choice
    # 입력상자의 갯수
    extra = 4
    # 해당 클래스를 생성한 후 QuestionChanger클래스에 등록해야한다.


class QuestionChanger(admin.ModelAdmin):
    fieldsets = [
        ("질문을 입력하세요", {"fields": ["question_text"]}),
        ("날짜를 입력하세요", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    # 4-1 : 4번 클래스를 생성한 후 이와같이 등록한다.
    # 그러면 질문과 답변 항목을 한 화면에서 등록할 수 있어 편리하다.
    inlines = [ChoiceInline]


"""
models.py 에서 테이블을 생성하면 관리자모드에 적용하기 위해 아래와
같이 등록절차가 필요하다. 이때 테이블은 클래스로 표현되므로 상단에
import구문이 필요하다.
"""
admin.site.register(Question, QuestionChanger)
admin.site.register(Choice)
