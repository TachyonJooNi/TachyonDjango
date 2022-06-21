# Create your models here.
from django.db import models
import os
from django.conf import settings


class Post(models.Model):
    titles = models.CharField(max_length=50)
    contents = models.TextField()
    mainphoto = models.ImageField(blank=True, null=True)

    """
    이 부분이 없으면 게시물 제목이 나오지 않고 Post object(1), (2)로 나온다.
    """

    def __str__(self):
        return self.titles

    """
    만약 delete()함수를 오버라이딩 하지 않으면 호출시 레코드만 삭제된다.
    하지만 파일삭제를 위해 오버라이딩 하여 파일까지 삭제할 수 있도록 재정의한다.
    """

    def delete(self, *args, **kargs):
        # 첨부된 파일이 있을때만 삭제 처리한다.
        if self.mainphoto:
            # 확인용 로그 출력(System.out.println()과 동일하다.)
            print("이미지 삭제")
            # 이미지가 저장된 media폴더와 삭제할 파일명 출력
            print(settings.MEDIA_ROOT, self.mainphoto.path)
            # 여기서 파일 삭제
            os.remove(os.path.join(settings.MEDIA_ROOT, self.mainphoto.path))
        # 여기서 레코드 삭제(원래 가지고있는 기능(위에 우리가 쓴건 오버라이딩으로 추가한 기능))
        super(Post, self).delete(*args, **kargs)
