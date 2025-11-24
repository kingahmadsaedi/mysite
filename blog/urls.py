from django.urls import path
from blog.views import *
app_name = 'blog'

urlpatterns = [
    path('',blog_view,name='index'),
    path('<int:pid>',blog_single,name='single'),
    path('category/<str:cat_name>',blog_view,name='category'),
    path('auther/<str:auther_username>',blog_view,name='auther'),
    path('search/',blog_search,name='search'),
    path('test',test_view,name='test')

]