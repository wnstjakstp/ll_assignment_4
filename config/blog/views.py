from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator

# READ
def home(request): # view로 넘어와서 models에서 처리해줌
    blogs = Blog.objects.all() # 블로그에서 모든 객체를 가져와라 (모델에서 정의되어있음)
    paginator = Paginator(blogs, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj}) # 결과물을 template에 담아서 줘야함
    # home.html이 template이다 blogs라는 변수에 blogs를 담아서 html로 보낸다
    # render는 response 객체로 만들어주는 것 

# DETAIL READ
def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog}) # detail.html으로 넘어간다 


# CREATE
def new(request):
    return render(request, 'new.html')


def create(request): # title과 content를 받아옴
    new_blog = Blog() # 빈 Model 객체를 생성
    new_blog.title = request.POST['title']
    new_blog.content = request.POST['content']
    new_blog.image = request.FILES.get('image') # 이미지 저장할 땐 get으로 이미지 없을 때 에러방지
    new_blog.save() # save는 저장 id 생성됨

    return redirect('detail', new_blog.id) # POST 요청을 GET 요청으로 바꿔서 계속 보내는 요청이 안생기게끔 해줌
    # return render(request, 'detail.html', {'blog': new_blog})
    # 보내느 요청 post 받는 요청 GET
    # redirect는 보내주는 것 blog id를 들고 detail이라는 url로 가라 view의 detail이 아니다 


# UPDATE
def edit(request, blog_id):
    edit_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'edit.html', {'edit_blog':edit_blog})


def update(request, blog_id): # update도 POST 요청이다
    old_blog = get_object_or_404(Blog, pk=blog_id)
    old_blog.title = request.POST.get('title')
    old_blog.content = request.POST.get('content')
    old_blog.image = request.FILES.get('image')
    old_blog.save()
    return redirect('detail', old_blog.id)
    # return render(request, 'detail.html', {'blog': old_blog})


# DELETE
def delete(request, blog_id):
    delete_blog = get_object_or_404(Blog, pk=blog_id)
    delete_blog.delete()
    return redirect('home')


# 보내는 요청 post
# 받는 요청 get
# detail page로 돌려줌 post를 get요청으로 바꿨음
# 요청을 안바꾸면 계속 로딩된다 ((ex)돈 송금)
# 계속 post를 보내면 안되는 상황도 있기 때문에 redirect를 쓴다
# render 요청은 url을 안바꾸고 화면인 html만 바꾸고 가져온다 
# render는 딕셔너리 형태로 가져온다 