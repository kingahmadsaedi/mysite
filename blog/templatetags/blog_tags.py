from django import template
from blog.models import Post
register = template.Library()

@register.simple_tag(name='totalposts')
def function():
    posts=Post.objects.filter(status=1)#.count()
    return posts
@register.filter
def snippest(value,arg=20):
    return value[:arg]+ ' ...'
@register.inclusion_tag('popularposts.html')
def popularposts():
    posts=Post.objects.filter(status=1).order_by('publish_date')[:1]
    return {'posts':posts}
@register.inclusion_tag('blog/latest-posts.html')
def latestposts(arg=3):
    posts=Post.objects.filter(status=1).order_by('publish_date')[:arg]
    return {'posts':posts}


