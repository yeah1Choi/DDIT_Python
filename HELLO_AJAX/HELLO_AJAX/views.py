from django.shortcuts import render
from django.http.response import JsonResponse
from flask import json
from django.views.decorators.csrf import csrf_exempt
from HELLO_AJAX.daoemp import DaoEmp


@csrf_exempt
def ajax(request):
    dict = json.loads(request.body)
    # do something
    print(dict['e_id'])

    context = {
        'result': dict,
    }
    return JsonResponse(context)

@csrf_exempt
def ajax_selectlist(request):
    
    de = DaoEmp()
    list = de.selectlist()

    json = {
        'list': list
    }
    return JsonResponse(json)

@csrf_exempt
def ajax_insert(request):
    e_id = request.POST['e_id']
    e_name = request.POST['e_name']
    gen = request.POST['gen']
    addr = request.POST['addr']
    
    de = DaoEmp()
    cnt = de.insert(e_id, e_name, gen, addr)

# controller에서 직접 list 함수 호출도 가능하고
# view에서 이런 식으로 직접 미리 작성도 가능하다.
    json = None;
    list = None;
    if cnt == 1 :
        list = de.selectlist()
        json = {
            'list' : list,
            'cnt': cnt
        }
    else :
        json = {
            'cnt': cnt
        }
    return JsonResponse(json)

@csrf_exempt
def ajax_update(request):
    e_id = request.POST['e_id']
    e_name = request.POST['e_name']
    gen = request.POST['gen']
    addr = request.POST['addr']
    
    de = DaoEmp()
    cnt = de.update(e_id, e_name, gen, addr)

    json = {
        'cnt': cnt
    }
    return JsonResponse(json)

@csrf_exempt
def ajax_delete(request):
    e_id = request.POST['e_id']
    
    de = DaoEmp()
    cnt = de.delete(e_id)

    json = {
        'cnt': cnt
    }
    return JsonResponse(json)

@csrf_exempt
def ajax_select(request):
    e_id = request.POST['e_id']
    
    de = DaoEmp()
    vo = de.selectOne(e_id)

    json = {
        'vo': vo
    }
    return JsonResponse(json)



