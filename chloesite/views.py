from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {}
    return render(request, 'chloesite/index.html', context)


def resume(request):
    context = {}
    return render(request, 'chloesite/resume.html', context)
