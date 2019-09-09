from django.http import HttpResponseRedirect
from django.shortcuts import render


# this is tha HomePage
from django.urls import reverse


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('accounts:panel', kwargs=dict(username=request.user.username)))
    else:
        return render(request, 'layout.html')
