from email import message
from unicodedata import category
from django.shortcuts import render,get_object_or_404
from django.urls import is_valid_path
from blog.models import Post,Comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from blog.forms import CommentForm

from django.contrib import messages
# Create your views here.
def blog_view(request,**kwargs):
    posts=Post.objects.filter(status=1)
    if kwargs.get('cat_name') !=None:
        posts=posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('tag_name') !=None:
        posts=posts.filter(tags__name__in=kwargs['tag_name'])
    if kwargs.get('auther_username') !=None:
        posts=posts.filter(auther__username=kwargs['auther_username'])
    posts=Paginator(posts,3)
    try:
        page_number=request.GET.get('page')
        posts=posts.get_page(page_number)
    except PageNotAnInteger:
        posts=posts.get_page(1)
    except EmptyPage:
        posts=posts.get_page(1)
    context={'posts':posts}
    print(context)
    return render(request,'blog/blog-home.html',context)
def blog_single(request,pid):
    
    if request.method == 'POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your comment submited successfully')
        else:
            messages.add_message(request,messages.ERROR,'your comment didnt submited !!!')
    
    posts=Post.objects.filter(status=1)
    post=get_object_or_404(posts,pk=pid)
    comments=Comment.objects.filter(post=post.id,approved=True)
    form=CommentForm()
    context={'post':post,'comments':comments,'form':form}
    return render(request,'blog/blog-single.html',context)
def blog_search(request):
    posts=Post.objects.filter(status=1)
    if request.method=='GET':
        if s:=request.GET.get('s'):
            posts=posts.filter(content__contains=s)
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)
def test_view(request):
    
    #post=Post.objects.get(id=pid)
    #post=get_object_or_404(posts,pk=pid)
    #context={'post':post}
    return render(request,'blog/test-view.html')
#def blog_category(request,cat_name):
    #posts=Post.objects.filter(status=1)
    #posts=posts.filter(category__name=cat_name)
    #context={'posts':posts}
    #return render(request,'blog/blog-home.html',context)