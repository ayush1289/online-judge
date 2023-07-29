from django.shortcuts import render, redirect
from .models import Problem, submissions
from OJ.compiler import compile_code, check_tc, run_code
from django.http import JsonResponse
import json



from pathlib import Path
import os

BASEDIR = Path(__file__).resolve().parent.parent


def home(request):
    questions = Problem.objects.all()
    return render(request, "index.html", {"questions": questions})


def problem(request, problem_id):
    question = Problem.objects.get(pk=problem_id)
    return render(request, "question.html", {"question": question})


def verdict(request, problem_id):
    question = Problem.objects.get(pk=problem_id)
    tc = Problem.objects.get(pk=problem_id).test_cases.all()

    if request.method == "POST":
        payload = json.loads(request.body)

        code = payload.get("code")
        language = payload.get("language")

        if code == "":
            return JsonResponse({"message": "code is empty"}, status=400)
        else:
            path = os.path.join(BASEDIR, f"OJ/waste/temp.{language}")
            with open(path, "w") as f:
                f.write(str(code))
            answer = compile_code(path, language)
            if answer != "Compilation successful":
                submission = submissions(
                    user_id=request.user.username,
                    problem_name=question.problem_name,
                    language=language,
                    code=code,
                    verdict=answer,
                )
                submission.save()
                return JsonResponse({"message": answer}, status=200)
            else:
                answer = check_tc(tc, language)
                if answer == "Accepted":
                    verdict = 1
                else:
                    verdict = 0

                submission = submissions(
                    user_id=request.user.username,
                    problem_name=question.problem_name,
                    language=language,
                    code=code,
                    verdict=answer,
                )
                submission.save()
                return JsonResponse({"message": answer}, status=200)
    else:
        return JsonResponse({"message": "Invalid Request"}, status=400)


def sub(request):
    submissions_list = submissions.objects.all()
    return render(request, "submissions.html", {"submissions_list": submissions_list})


def customTc(request):
    if request.method == "POST":
        payload = json.loads(request.body)
        user_tc_value = payload.get("user_tc")
        code = payload.get("user_code")
        language = payload.get("language")

        if code == "":
            return JsonResponse({"message": "user_tc is empty"}, status=400)
        else:
            path = os.path.join(BASEDIR, f"OJ/waste/temp.{language}")
            with open(path, "w") as f:
                f.write(str(code))

            answer = compile_code(path, language)
            if answer != "Compilation successful":
                return JsonResponse({"message": answer}, status=200)
            else:
                answer = run_code(language, str(user_tc_value).replace(" ", "\n"))
                return JsonResponse({"message": answer}, status=200)
    else:
        return JsonResponse({"message": "Invalid request"}, status=400)
    