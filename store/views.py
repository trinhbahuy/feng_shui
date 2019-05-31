from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from django.template import loader

from django.urls import reverse

def index(request):
	question = "xxx"
	return render(request, 'store/index.html', {'question': question})