from django.shortcuts import render
from django.http import HttpResponse

# note: the command "startapp" will generate a  number of code files and one subfolder.

# Of these, you frequently work with views.py (that contains the functions that define pages in your web app) and models.py (that contains classes defining your data objects).

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")