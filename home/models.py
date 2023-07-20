from django.db import models

# Create your models here.
class test_case(models.Model):
    tc_input = models.CharField(max_length=200)
    tc_output = models.CharField(max_length=200)


class Problem(models.Model):
    problem_id = models.IntegerField(primary_key=True)
    problem_name = models.CharField(max_length=100)
    problem_description = models.TextField()
    test_cases = models.ManyToManyField(test_case)

class submissions(models.Model):
    user_id = models.CharField(max_length=100)
    problem_name = models.CharField(max_length=100)
    language = models.CharField(max_length=10)
    code = models.TextField()
    verdict = models.BooleanField()
    time = models.DateTimeField(auto_now_add=True)






