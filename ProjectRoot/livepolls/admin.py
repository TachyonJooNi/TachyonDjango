# Register your models here.
from django.contrib import admin

"""
    형식] 앱의이름.models.py import 클래스명
        두개 이상의 클래스가 필요하면 컴마(,)로 구분하면 된다.
        해당 모듈은 model이므로 각 클래스명은 테이블을 의미한다.
"""
from livepolls.models import Question, Choice

"""
models.py 에서 테이블을 생성하면 관리자모드에 적용하기 위해 아래와
같이 등록절차가 필요하다. 이때 테이블은 클래스로 표현되므로 상단에
import구문이 필요하다.
"""
admin.site.register(Question)
admin.site.register(Choice)
