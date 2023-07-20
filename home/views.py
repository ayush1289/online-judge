from django.shortcuts import render,redirect
from .models import Problem
from OJ.compiler import compile_code,check_tc
from django.contrib import messages

BASEDIR = "/home/ayush/Documents/AlgoUni_Project/OJ/"

def home(request):
    questions = Problem.objects.all()
    return render(request,'index.html',{'questions':questions})

def problem(request,problem_id):
    question = Problem.objects.get(pk=problem_id)
    return render(request,'question.html',{'question':question})

def verdict(request,problem_id):
    question = Problem.objects.get(pk=problem_id)
    tc = Problem.objects.get(pk=problem_id).test_cases.all()

    if request.method == 'POST':
        code = request.POST['code']
        language = request.POST['language']
        ip = request.POST['ip']

        if code == "":
            messages.info(request,"Please enter the code")
            return redirect('problem',problem_id=problem_id)
        else:
            path = BASEDIR + f'OJ/waste/temp.{language}'
            with open(path,'w') as f:
                f.write(code)

            compile_code(path,language)

            answer = check_tc(tc,language)

            return render(request,'verdict.html',{'code':code,'question':question,'answer':answer})
    else:
        return redirect('problem',problem_id=problem_id)