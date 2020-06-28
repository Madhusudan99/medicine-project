from django.shortcuts import render
from django.http import HttpResponse
from formating import Text_to_speech

# Create your views here.
def index(request):
	if request.method == 'POST':
		obj = Text_to_speech()
		tts_data = obj.run_tts()
		text = tts_data
		return HttpResponse(text)