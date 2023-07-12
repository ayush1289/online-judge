from django.shortcuts import render
from .models import Problem

# Create your views here.

def home(request):
    questions = Problem.objects.all()
    return render(request,'index.html',{'questions':questions})

def problem(request,problem_id):
    question = Problem.objects.get(pk=problem_id)
    return render(request,'question.html',{'question':question})


