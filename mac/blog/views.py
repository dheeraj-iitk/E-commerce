from django.shortcuts import render
from .models import Blogpost
# Create your views here.
from django.http import HttpResponse

def index(request):
    allblogs=Blogpost.objects.all()
    params={'blogs':allblogs}
    return render(request, 'index3.html',params)

def blogpost(request,id):
    post = Blogpost.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'blogpost.html',
                  {'post':post})