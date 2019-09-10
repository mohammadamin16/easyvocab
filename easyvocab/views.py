from django.http import HttpResponseRedirect
from django.shortcuts import render


# this is tha HomePage
from django.urls import reverse
from django.views.generic.base import TemplateView


class HomePage(TemplateView):
    template_name = 'layout.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('accounts:panel', kwargs=dict(username=request.user.username)))
        return super(HomePage, self).get(request, *args, **kwargs)
