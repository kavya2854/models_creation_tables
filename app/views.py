from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_dept(request):
    QLDO = Dept.objects.all()
    d = {'depts':QLDO}
    return render(request,'insert_dept.html',d)

def insert_emp(request):
    QLEO = Employee.objects.all()
    d = {'employees':QLEO}
    return render(request,'insert_emp.html',d)
    
def insert_salgrade(request):
    QLSGO = Salgrade.objects.all()
    d = {'salgrades':QLSGO}
    return render(request,'insert_salgrade.html',d)

def insert_bonus(request):
    QLBO = Bonus.objects.all()
    d = {'bonuss':QLBO}
    return render(request,'insert_bonus.html',d)

def inserting_dept(request):
    dn = int(input('Enter deptno : '))
    d_name = input('Enter deptname : ')
    d_loc = input('Enter location : ')
    DO = Dept.objects.get_or_create(deptno = dn,dname = d_name,loc = d_loc)[0]
    DO.save()
    return HttpResponse('Dept is created')

def inserting_emp(request):
    en = int(input('Enter Empno : '))
    e_name = input('Enter Ename : ')
    e_job = input('Enter job : ')
    MGR = int(input('Enter mgr : '))
    hd = input('Enter hiredate : ')
    salary = int(input('Enter sal : '))
    commission =  int(input('Enter comm : '))
    dn = int(input('Enter dn : '))
    DO = Dept.objects.get(deptno = dn)
    EO = Employee.objects.get_or_create(empno = en,ename = e_name,job = e_job,mgr = MGR,hiredate = hd,sal = salary,comm = commission,deptno = DO)[0]
    EO.save()
    return HttpResponse('Employee Table is Created')

def inserting_salgrade(request):
    gr = int(input('Enter grade : '))
    lowsal = int(input('Enter losal : '))
    highsal = int(input('Enter hisal : '))
    SGO = Salgrade.objects.get_or_create(grade = gr,losal = lowsal,hisal = highsal)[0]
    SGO.save()
    return HttpResponse('Salgrade is created')

def inserting_bonus(request):
    en = input('Enter ename : ')
    j = input('Enter job : ')
    salary = int(input('Enter sal : '))
    commission = int(input('Enter comm : '))
    NBO = Bonus.objects.get_or_create(ename = en,job = j,sal = salary,comm = commission)[0]
    NBO.save()
    return HttpResponse('Bonus Table is Created')

    