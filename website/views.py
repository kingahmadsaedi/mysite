from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index_view(request):
    return HttpResponse('<h1>this is index page</h1>')
def about_view(request):
    return HttpResponse('<h1>this is about page</h1>')
def contact_view(request):
    return HttpResponse('<h1>this is contact page</h1>')