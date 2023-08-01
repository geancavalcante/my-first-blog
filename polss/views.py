from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("olá,mundo")

def eae (request):
    return HttpResponse('eaeeee')

def opa(request):
    return HttpResponse('opaaaaaaa')