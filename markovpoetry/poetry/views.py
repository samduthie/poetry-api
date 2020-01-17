from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from poetry.poetry import generate_sentence

class IndexView(View):
	def get(self, request):
		poetry_sentence = generate_sentence()
		context = {
		    'sentence': poetry_sentence
		}

		return render(request, 'poetry/index.html', context)