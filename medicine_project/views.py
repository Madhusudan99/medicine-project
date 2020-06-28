from django.shortcuts import render
from django.http import HttpResponse
from formating import Text_to_speech

# Create your views here.
def homepage(request):
	# return HttpResponse("Hello World. You're at the homepage")
	return render(request, 'homepage.html')


def about(request):
	# return HttpResponse("About us")
	return render(request, 'about.html')
