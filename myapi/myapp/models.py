from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    standard = models.IntegerField()
