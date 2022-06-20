# Create your models here.
from django.db import models

# 책 테이블 생성
class Book(models.Model):
    # 책의 제목
    title = models.CharField(max_length=100)
    # 저자이름 : Author 테이블의 PK와 N:N의 관계를 설정한다.
    #   한명의 저자가 여러권의 책을 쓸 수 있다.
    authors = models.ManyToManyField('Author')
    # 출판사 : Publisher 테이블의 PK와 1:N의 관계를 설정한다.
    #   책은 한 출판사에서만 출간된다.
    #   models.CASCADE옵션은 오라클과 동일하게 부모레코드가 삭제될때 자식까지 같이 삭제된다.
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    # 출판일 (아래 둘중에 하나 쓰면 된다.)
    # publication_date = models.DateTimeField('date published') # 일종의 설명문
    publication_date = models.DateField()
    
    # 해당 함수가 없으면 관리자에서 테이블명이 제대로 표시되지 않는다.
    def __str__(self):
        return self.title
    
# 저자 테이블 생성
class Author(models.Model):
    # 이름
    name = models.CharField(max_length=50)
    # 인사말
    salutation = models.CharField(max_length=100)
    # 이메일
    email = models.EmailField()
    
    def __str__(self):
        return self.name

# 출판사 테이블 생성
class Publisher(models.Model):
    # 출판사명
    name = models.CharField(max_length=50)
    # 주소
    address = models.CharField(max_length=100)
    # 웹사이트 URL
    website = models.URLField()
    
    def __str__(self):
        return self.name
    