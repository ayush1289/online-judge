from django.shortcuts import render,redirect
from .models import Problem
from OJ.compiler import save_text_file,change_file_extension,change_file_name



# Create your views here.

def home(request):
    questions = Problem.objects.all()
    return render(request,'index.html',{'questions':questions})

def problem(request,problem_id):
    question = Problem.objects.get(pk=problem_id)
    return render(request,'question.html',{'question':question})

# saving the file in the waste folder present in the OJ folder
def verdict(request,problem_id):
    question = Problem.objects.get(pk=problem_id)
    path = f'/home/ayush/Documents/AlgoUni_Project/OJ/OJ/waste/{question.problem_name}.txt'
    if request.method == 'POST':
        code = request.POST['code']
        language = request.POST['language']
        save_text_file(path,str(code))
        change_file_name(path,f'{question.problem_name}.txt')
        change_file_extension(path,language)
        return render(request,'verdict.html',{'code':code,'question':question})
    else:
        return redirect('problem',problem_id=problem_id)