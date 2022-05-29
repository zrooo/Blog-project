from django.shortcuts import redirect, render, get_object_or_404
from .models import Blog
from django.utils import timezone

# Create your views here.
def home(request):
    #블로그 글들 전부 띄우는 코드
    posts = Blog.objects.all()
    return render(request, 'index.html', {'posts': posts})

#블로그 글 작성 html 보여 주는 함수
def new(request):
   return render(request, 'new.html')

#블로그 글 저장해 주는 함수
def create(request):
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home') #redirect: 다시 보내다, 이 함수가 다 실행됐으면 index.html로 다시 가라

def detail(request, blog_id):
    #blog_id번째 블로그 글을 데이터베이스로부터 갖고 와서 detail.html로 띄우는 코드
    blog_detail = get_object_or_404(Blog, pk=blog_id)   #pk값이 blog_id인 Blog 객체를 가져와라, 없으면 404 not found
    return render(request, 'detail.html', {'blog_detail':blog_detail})
