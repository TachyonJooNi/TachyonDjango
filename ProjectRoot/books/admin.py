# Register your models here.
from django.contrib import admin
# 등록시에는 해당 테이블들을 임포트 해야한다.
from books.models import Author, Book, Publisher

# 생성된 테이블을 관리자페이지에 등록한다.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)

