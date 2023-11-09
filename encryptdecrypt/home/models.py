from django.db import models

# Create your models here.

class StudentsMarks(models.Model):
    name=models.CharField(max_length=40)
    usn=models.CharField(max_length=10)
    phonenumber = models.CharField(max_length=10)
    email = models.CharField(max_length=40)
    marks1 = models.IntegerField(default=0)
    marks2 = models.IntegerField(default=0)
    marks3 = models.IntegerField(default=0)
    marks4 = models.IntegerField(default=0)
    marks5 = models.IntegerField(default=0)
    marks6 = models.IntegerField(default=0)
    marks7 = models.IntegerField(default=0)
    datetime=models.DateTimeField(auto_now=True)
    totalmarks=models.IntegerField(default=0)

    def __str__(self):
        return self.name

