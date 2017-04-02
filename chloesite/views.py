from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {}
    return render(request, 'chloesite/index.html', context)

def detail(request, question_id):
	return HttpResponse("Question #%s" % question_id)
