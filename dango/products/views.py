from django.http import HttpResponse
from django.shortcuts import render

'''
how to use:

1.define page name and add bracketes
and request inside then add colon

2.indent then write return HttpResponse in bracketes what you
want displayed



'''





def index(request):
    return HttpResponse("hello world")

def new(request):
    return HttpResponse("New products")


def rename(request):
    return HttpResponse("rename")

def rename(request):
    return HttpResponse("rename")

