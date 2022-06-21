from django.shortcuts import redirect, render
from board.models import Post
import os
from django.conf import settings

# Create your views here.

# 게시판 앱의 첫화면(원래 로켓화면)
def index(request):
    return render(request, "board/index.html")


# 게시판 목록(페이지처리 X)
def list(request):
    # Post테이블의 모든 레코드를 id(일련번호:PK)의 내림차순으로 가져온다.
    postlist = Post.objects.all().order_by("-id")
    # 템플릿 렌더링시 컨텍스트 변수 전달
    return render(request, "board/list.html", {"postlist": postlist})


# 글쓰기 페이지 진입 / 글쓰기 처리
def write(request):
    # 전송방식이 POST라면 submit이므로 폼값을 테이블에 입력한다.
    if request.method == "POST":
        try:
            Post.objects.create(
                titles=request.POST["titles"],
                contents=request.POST["contents"],
                # 만약 파일첨부를 하지 않으면 여기서 예외가 발생하여
                # except절로 넘어가게 된다.
                mainphoto=request.FILES["mainphoto"],
            )
        except:
            # 파일첨부를 하지 않는 경우이므로 제목과 내용만 입력한다.
            Post.objects.create(
                titles=request.POST["titles"],
                contents=request.POST["contents"],
            )
        # 입력 처리가 완료되었다면 리스트로 이동한다.
        return redirect("/board/list")
    # 전송방식이 POST가 아니라면 글쓰기 페이지 진입을 위해 랜더링한다.
    return render(request, "board/write.html")


# 글 상세보기
def view(request, pk):
    # 일련번호(PK)에 해당하는 게시물 하나를 selet 한다.
    post = Post.objects.get(pk=pk)
    # 가져온 게시물을 컨텍스트 변수로 전달한다.
    return render(request, "board/view.html", {"post": post})


# 글 수정하기
def edit(request, pk):
    # 일련번호에 해당하는 기존 게시물 가져오기
    post = Post.objects.get(pk=pk)

    if request.method == "POST":
        # 전송방식이 POST라면 submit이므로 수정처리
        try:
            # 첨부파일이 있는 경우 수정
            post.titles = request.POST["titles"]
            post.contents = request.POST["contents"]
            post.mainphoto = request.FILES["mainphoto"]

            # 새로운 파일을 등록하는 경우라면 기존 파일을 삭제처리해야 한다.
            # 해당 함수는 models.py에서 작성된 내용과 동일하다.
            # 물리적경로와 파일명을 join()하여 파일을 삭제처리한다.
            print(os.path.join(settings.MEDIA_ROOT, request.POST["prevphoto"]))
            os.remove(os.path.join(settings.MEDIA_ROOT, request.POST["prevphoto"]))
        except:
            print("여기니?")
            # 첨부파일이 없는 예외가 발생한 경우 수정처리
            post.titles = request.POST["titles"]
            post.contents = request.POST["contents"]
        # 폼값 처리 후 save()함수를 통해 update 처리한다.
        post.save()
        # 수정 처리가 완료되면 상세보기 페이지로 이동한다.
        return redirect("/board/view/" + str(pk) + "/")
    else:
        # GET방식이면 수정페이지로 진입한다. 이때 게시물을 컨텍스트 변수로 넘긴다.
        return render(request, "board/edit.html", {"post": post})


# 게시물 삭제
def delete(request, pk):
    # 기존 게시물 얻어오기
    post = Post.objects.get(pk=pk)
    if request.method == "GET":
        # 게시물 삭제(모델의 레코드를 삭제한다는 의미). (models.py 에 있음)
        post.delete()
        return redirect("/board/list/")
