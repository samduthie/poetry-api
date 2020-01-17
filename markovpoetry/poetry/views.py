from django.http import HttpResponse
from django.views import View

from poetry.poetry import generate_sentence

class IndexView(View):
	def get(self, request):
		poetry_sentence = generate_sentence()
		return HttpResponse(poetry_sentence)