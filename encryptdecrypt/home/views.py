from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from datetime import datetime
from . import models

usn=None
def home(request):
   global usn
   if request.method == 'POST':
      name = request.POST['studentname']
      usn = request.POST['usn']
      phonenumber = request.POST['phonenumber']
      ins = models.StudentsMarks(name=name, usn = usn , phonenumber=phonenumber)
      ins.save()
      return HttpResponseRedirect('/question1')
   return render(request,'index.html')

def question1(request):
   global usn
   print("Question 1")
   print(usn)
   print("Question 1")
   if request.method == 'POST':
       ans=request.POST['questionans']
       marks=0
       if ans=='1':
           marks=10
           allobjects = models.StudentsMarks.objects.get(usn=usn)
           name = allobjects.name
           usn = allobjects.usn
           phonenumber = allobjects.phonenumber
           marks1 = marks
           marks2 = allobjects.marks2
           marks3 = allobjects.marks3
           marks4 = allobjects.marks4
           marks5 = allobjects.marks5
           marks6 = allobjects.marks6
           marks7 = allobjects.marks7
           totalmarks = int(marks7) + int(marks6) + int(marks5) + int(marks4) + int(marks1) + int(marks2) + int(marks3)
           ins = models.StudentsMarks(name=name, usn=usn, phonenumber=phonenumber,marks7=marks7,marks6=marks6,marks5=marks5,marks4=marks4,marks3=marks3,marks1=marks1,marks2=marks2,totalmarks=totalmarks,datetime=datetime.now())
           models.StudentsMarks.objects.filter(usn=usn).delete()
           ins.save()
       return HttpResponseRedirect('/question2')
   context={"context": models.StudentsMarks.objects.filter(usn=usn)}
   return render(request,'question1.html',context=context)

def question2(request):
   global usn
   print("Question 2")
   print(usn)
   print("Question 2")
   if request.method == 'POST':
       ans=request.POST['questionans']
       marks=0
       if ans=='1':
           marks=10
           allobjects = models.StudentsMarks.objects.get(usn=usn)
           name = allobjects.name
           usn = allobjects.usn
           phonenumber = allobjects.phonenumber
           marks1 = allobjects.marks1
           marks2 = marks
           marks3 = allobjects.marks3
           marks4 = allobjects.marks4
           marks5 = allobjects.marks5
           marks6 = allobjects.marks6
           marks7 = allobjects.marks7
           totalmarks=int(marks7)+int(marks6)+int(marks5)+int(marks4)+int(marks1)+int(marks2)+int(marks3)
           ins = models.StudentsMarks(name=name, usn=usn, phonenumber=phonenumber,marks7=marks7,marks6=marks6,marks5=marks5,marks4=marks4,marks3=marks3,marks1=marks1,marks2=marks2,totalmarks=totalmarks,datetime=datetime.now())
           models.StudentsMarks.objects.filter(usn=usn).delete()
           ins.save()
       return HttpResponseRedirect('/question3')
   context={"context": models.StudentsMarks.objects.filter(usn=usn)}
   return render(request,'question2.html',context=context)

def question3(request):
   global usn
   print("Question 3")
   print(usn)
   print("Question 3")
   if request.method == 'POST':
       ans=request.POST['questionans']
       marks=0
       if ans=='1':
           marks=10
           allobjects = models.StudentsMarks.objects.get(usn=usn)
           name = allobjects.name
           usn = allobjects.usn
           phonenumber = allobjects.phonenumber
           marks1 = allobjects.marks1
           marks2 = allobjects.marks2
           marks3 = marks
           marks4 = allobjects.marks4
           marks5 = allobjects.marks5
           marks6 = allobjects.marks6
           marks7 = allobjects.marks7
           totalmarks = int(marks7) + int(marks6) + int(marks5) + int(marks4) + int(marks1) + int(marks2) + int(marks3)
           ins = models.StudentsMarks(name=name, usn=usn, phonenumber=phonenumber,marks7=marks7,marks6=marks6,marks5=marks5,marks4=marks4,marks3=marks3,marks1=marks1,marks2=marks2,totalmarks=totalmarks,datetime=datetime.now())
           models.StudentsMarks.objects.filter(usn=usn).delete()
           ins.save()
       return HttpResponseRedirect('/question4')
   context={"context": models.StudentsMarks.objects.filter(usn=usn)}
   return render(request,'question3.html',context=context)

def question4(request):
   global usn
   print("Question 4")
   print(usn)
   print("Question 4")
   if request.method == 'POST':
       ans=request.POST['questionans']
       marks=0
       if ans=='1':
           marks=10
           allobjects = models.StudentsMarks.objects.get(usn=usn)
           name = allobjects.name
           usn = allobjects.usn
           phonenumber = allobjects.phonenumber
           marks1 = allobjects.marks1
           marks2 = allobjects.marks2
           marks3 = allobjects.marks3
           marks4 = marks
           marks5 = allobjects.marks5
           marks6 = allobjects.marks6
           marks7 = allobjects.marks7
           totalmarks=int(marks7)+int(marks6)+int(marks5)+int(marks4)+int(marks1)+int(marks2)+int(marks3)
           ins = models.StudentsMarks(name=name, usn=usn, phonenumber=phonenumber,marks7=marks7,marks6=marks6,marks5=marks5,marks4=marks4,marks3=marks3,marks1=marks1,marks2=marks2,totalmarks=totalmarks,datetime=datetime.now())
           models.StudentsMarks.objects.filter(usn=usn).delete()
           ins.save()
       return HttpResponseRedirect('/question5')
   context={"context": models.StudentsMarks.objects.filter(usn=usn)}
   return render(request,'question4.html',context=context)

def question5(request):
   global usn
   print("Question 5")
   print(usn)
   print("Question 5")
   if request.method == 'POST':
       ans=request.POST['questionans']
       marks=0
       if ans=='1':
           marks=10
           allobjects = models.StudentsMarks.objects.get(usn=usn)
           name = allobjects.name
           usn = allobjects.usn
           phonenumber = allobjects.phonenumber
           marks1 = allobjects.marks1
           marks2 = allobjects.marks2
           marks3 = allobjects.marks3
           marks4 = allobjects.marks4
           marks5 = marks
           marks6 = allobjects.marks6
           marks7 = allobjects.marks7
           totalmarks = int(marks7) + int(marks6) + int(marks5) + int(marks4) + int(marks1) + int(marks2) + int(marks3)
           ins = models.StudentsMarks(name=name, usn=usn, phonenumber=phonenumber,marks7=marks7,marks6=marks6,marks5=marks5,marks4=marks4,marks3=marks3,marks1=marks1,marks2=marks2,totalmarks=totalmarks,datetime=datetime.now())
           models.StudentsMarks.objects.filter(usn=usn).delete()
           ins.save()
       return HttpResponseRedirect('/question6')
   context={"context": models.StudentsMarks.objects.filter(usn=usn)}
   return render(request,'question5.html',context=context)

def question6(request):
   global usn
   print("Question 6")
   print(usn)
   print("Question 6")
   if request.method == 'POST':
       ans=request.POST['questionans']
       marks=0
       if ans=='1':
           marks=10
           allobjects = models.StudentsMarks.objects.get(usn=usn)
           name = allobjects.name
           usn = allobjects.usn
           phonenumber = allobjects.phonenumber
           marks1 = allobjects.marks1
           marks2 = allobjects.marks2
           marks3 = allobjects.marks3
           marks4 = allobjects.marks4
           marks5 = allobjects.marks5
           marks6 = marks
           marks7 = allobjects.marks7
           totalmarks=int(marks7)+int(marks6)+int(marks5)+int(marks4)+int(marks1)+int(marks2)+int(marks3)
           ins = models.StudentsMarks(name=name, usn=usn, phonenumber=phonenumber,marks7=marks7,marks6=marks6,marks5=marks5,marks4=marks4,marks3=marks3,marks1=marks1,marks2=marks2,totalmarks=totalmarks,datetime=datetime.now())
           models.StudentsMarks.objects.filter(usn=usn).delete()
           ins.save()
       return HttpResponseRedirect('/question7')
   context={"context": models.StudentsMarks.objects.filter(usn=usn)}
   return render(request,'question6.html',context=context)

def question7(request):
   global usn
   print("Question 7")
   print(usn)
   print("Question 7")
   if request.method == 'POST':
       ans=request.POST['questionans']
       marks=0
       if ans=='1':
           marks=10
           allobjects = models.StudentsMarks.objects.get(usn=usn)
           name = allobjects.name
           usn = allobjects.usn
           phonenumber = allobjects.phonenumber
           marks1 = allobjects.marks1
           marks2 = allobjects.marks2
           marks3 = allobjects.marks3
           marks4 = allobjects.marks4
           marks5 = allobjects.marks5
           marks6 = allobjects.marks6
           marks7 = marks
           totalmarks=int(marks7)+int(marks6)+int(marks5)+int(marks4)+int(marks1)+int(marks2)+int(marks3)
           ins = models.StudentsMarks(name=name, usn=usn, phonenumber=phonenumber,marks7=marks7,marks6=marks6,marks5=marks5,marks4=marks4,marks3=marks3,marks1=marks1,marks2=marks2,totalmarks=totalmarks,datetime=datetime.now())
           models.StudentsMarks.objects.filter(usn=usn).delete()
           ins.save()
       return HttpResponseRedirect('/question1')
   context={"context": models.StudentsMarks.objects.filter(usn=usn)}
   return render(request,'question7.html',context=context)

def leaderboard(request):
   allobjects = models.StudentsMarks.objects.all().order_by('-totalmarks','datetime')
   context={"context":allobjects}
   return render(request,'leaderboard.html',context=context)