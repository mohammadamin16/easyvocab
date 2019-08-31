from django.http import HttpResponse
from django.shortcuts import render


# this is tha HomePage
def index(request):
    return render(request, 'layout.html')
