from django.shortcuts import render
from django.http import HttpResponse

def post_list(request):
    return render(request, 'blog/post_list.html',{})

def eae (request):
    return HttpResponse('eaeeee')

def opa(request):
    return HttpResponse('opaaaaaaa')