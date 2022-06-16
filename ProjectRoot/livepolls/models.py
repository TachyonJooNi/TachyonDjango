# Create your models here.
from django.db import models


"""
장고에서는 테이블을 하나의 클래스로 정의하고, 테이블의 컬럼은
클래스의 변수로 매핑한다.
django.db.models.Model 클래스를 상속받아 정의하고, 각 클래스 변수의
타입도 장고에서 미리 정의해둔 필드 클래스를 사용한다.
"""

# Question 테이블 생성 : 설문에 대한 질문을 입력한다.
class Question(models.Model):
    """
    PK(기본키)는 별도로 지정하지 않아도 장고에서 자동으로 생성해준다.
    컬럼명은 id로 not null, AutoIncrement 제약조건이 추가된다.
    """

    # 질문항목 : varchar(200) 와 같이 문자형으로 선언한다.
    question_text = models.CharField(max_length=200)
    # 등록날짜 : datetime으로 지정함. 뒤의 문자열은 일종의 설명문이다.
    pub_date = models.DateTimeField("date published")

    """
    객체를 문자열로 표현할때 사용한다. 해당 함수를 정의하지 않으면 테이블명이
    제대로 표시되지 않는다.
    """

    def __str__(self):
        return self.question_text


# Choice 테이블 생성 : 질문에 대한 답변 항목
class Choice(models.Model):
    """
    FK는 항상 부모테이블의 PK와 연결되므로 Question 클래스만 지정하면 된다.
    FK로 지정된 컬럼은 자동으로 _id라는 접미사가 붙게된다.
    """

    # 외래키 설정
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 답변한목 : 문자형으로 생성
    choice_text = models.CharField(max_length=200)
    # 투표수 : 숫자형으로 생성
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
