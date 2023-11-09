from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
import pymysql
from HELLO_DJANGO import daoemp
from HELLO_DJANGO.daoemp import DaoEmp

def index(request):
    return HttpResponse("Hello Django!")

def param(request):
    return HttpResponse("PARAM")

def menu(request):
    menu = request.GET.get('menu', '탕수육')
    # 뒤에 오는 값은 파라미터가 없는 경우, 올 기본값이다.
    return HttpResponse(f"Today menu is {menu}")

@csrf_exempt
def post(request):
    menu = request.POST['menu']
    return HttpResponse("POST" + menu)

def forw(request):
    a = "홍길동"
    b = ["전우치", "일지매"]
    c = [
            {'e_id':1, 'e_name':1, 'gen':1, 'addr':1},
            {'e_id':2, 'e_name':2, 'gen':3, 'addr':4},
            {'e_id':2, 'e_name':2, 'gen':3, 'addr':4},
            {'e_id':2, 'e_name':2, 'gen':3, 'addr':4}
        ]
    return render(request, 'forw.html', {'a' : a, 'b' : b, 'c' : c})

def emp(request):
    de = DaoEmp()
    list = de.selectList()
    
    return render(request, 'emp.html', {'list' : list})


