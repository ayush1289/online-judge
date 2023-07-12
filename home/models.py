from django.db import models

# Create your models here.

class Problem(models.Model):
    problem_id = models.IntegerField(primary_key=True)
    problem_name = models.CharField(max_length=100)
    problem_description = models.TextField()



