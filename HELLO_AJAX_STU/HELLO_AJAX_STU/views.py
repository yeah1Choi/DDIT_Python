from django.shortcuts import render, redirect
from django.http.response import HttpResponse, HttpResponseRedirect,\
    JsonResponse
from HELLO_AJAX_STU.daostudent import DaoStudent
from django.views.decorators.csrf import csrf_exempt

def index(request):
    #return HttpResponse("Hello Django!")
    #return redirect('/static/student.html')
    return HttpResponse("<script>location.href='/static/student.html'</script>")

@csrf_exempt
def ajax_selectList(request):
    ds = DaoStudent()
    students = ds.selectList()

    json = {
        'students':students
    }
    return JsonResponse(json)

@csrf_exempt
def ajax_select(request):
    s_id = request.POST['s_id']
    
    ds = DaoStudent()
    student = ds.selectOne(s_id)

    json = {
        'student': student
    }
    return JsonResponse(json)

@csrf_exempt
def ajax_insert(request):
    s_id = request.POST['s_id']
    s_name = request.POST['s_name']
    mobile = request.POST['mobile']
    grade = request.POST['grade']
    
    ds = DaoStudent()
    cnt = ds.insert(s_id, s_name, mobile, grade)

    json = {
        'cnt': cnt
    }

    return JsonResponse(json)

@csrf_exempt
def ajax_update(request):
    s_id = request.POST['s_id']
    s_name = request.POST['s_name']
    mobile = request.POST['mobile']
    grade = request.POST['grade']
    
    ds = DaoStudent()
    cnt = ds.update(s_id, s_name, mobile, grade)

    json = {
        'cnt': cnt
    }
    return JsonResponse(json)

@csrf_exempt
def ajax_delete(request):
    s_id = request.POST['s_id']
    
    ds = DaoStudent()
    cnt = ds.delete(s_id)

    json = {
        'cnt': cnt
    }
    return JsonResponse(json)
