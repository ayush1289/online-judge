from django.shortcuts import render,redirect
from .models import Problem
from OJ.compiler import compile_code,run_code

import os
BASEDIR = "/home/ayush/Documents/AlgoUni_Project/OJ/"
# Create your views here.

def home(request):
    questions = Problem.objects.all()
    return render(request,'index.html',{'questions':questions})

def problem(request,problem_id):
    question = Problem.objects.get(pk=problem_id)
    print(question.problem_name)
    print(problem_id)
    return render(request,'question.html',{'question':question})

# saving the file in the waste folder present in the OJ folder
def verdict(request,problem_id):
    question = Problem.objects.get(pk=problem_id)
    path = BASEDIR + f'OJ/waste/{question.problem_id}.txt'
    if request.method == 'POST':
        code = request.POST['code']
        language = request.POST['language']
        ip = request.POST['ip']
        with open(path,'w') as f:
            f.write(code)
        oldpath = os.path.join(BASEDIR+'OJ/waste/',f'{question.problem_id}.txt')
        newpath = os.path.join(BASEDIR+'OJ/waste/',f'{question.problem_id}.{language}')
        os.rename(oldpath,newpath)
        compile_code(newpath,language)
        answer = run_code(BASEDIR+'OJ/waste',language,str(ip))
        return render(request,'verdict.html',{'code':code,'question':question,'answer':answer})
    else:
        return redirect('problem',problem_id=problem_id)