from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from . models import Task
from datetime import date
from random import randint
from .serializers import *

# Create your views here.

@api_view(['POST'])
def add_task(request):     
    try:
        params = request.data     
        task = params['task']
        description = params['description']
        description = request.POST['description']
        priority = request.POST['priority']
        today = date.today()
        user = Task(task=task,
                    priority = priority,
                    user_id = params['user'],
                    description=description,
                    date=today)        
        user.save()       
        return JsonResponse({'statusCode': 201,'msg':'Task Added'})
    except Exception as e:
        print(e)
        return JsonResponse({'statusCode': 500,'msg':'Something went wrong'})
    

@api_view(['GET'])
def task_list(request,status):

    user = request.GET['user']
    print(user, status)
    records = Task.objects.filter(user = user, status = status)
    if records:
        serialized_records = TaskSerializer(records,many = True)
        return JsonResponse({'statusCode':200,'tasks': serialized_records.data,'msg': 'Data Fetched'})
    return JsonResponse({'statusCode':404, 'tasks':[],'msg': 'No Records Found'})


 


@api_view(['GET'])
def filter_task(request):

    user = request.GET['user']
    priority = request.GET['priority']
    records = Task.objects.filter(user = user, priority = priority)
    if records:
        serialized_records = TaskSerializer(records,many = True)
        return JsonResponse({'statusCode':200,'sellers':serialized_records.data,'msg': 'Data Fetched'})
    return JsonResponse({'statusCode':404,'sellers':[],'msg' : 'No Records Found'})
    

@api_view(['GET'])
def search_task(request):
    user = request.GET['user']
    searchText = request.GET['query']
    print(user,searchText)
    records = Task.objects.filter(task__contains = searchText, user = user, status = 'completed')
    if records:
        serialized_records = TaskSerializer(records,many = True)
        return JsonResponse({'statusCode':200,'searchResult':serialized_records.data,'msg': 'Data Fetched'})
    return JsonResponse({'statusCode':404,'searchResult':[],'msg' : 'No Records Found'})
    

@api_view(['DELETE'])
def delete_task(request,id):

    try:
        records = Task.objects.get(id = id)
        records.delete()
        
        return JsonResponse({'statusCode':200,'msg':'Task Deleted Succesfully',})

    except Exception as e:
        print(e)
        return JsonResponse({'statusCode':500,'msg':'someting Went Wrong...',})



@api_view(['PUT'])
def update_task(request,id):
    try:

        params = request.data
        record = Task.objects.get(id = id)	
        serialized_record = TaskSerializer(record, data = params)
        if serialized_record.is_valid():
            serialized_record.save()
            return JsonResponse({'statusCode':202,'msg':'Task Updated',})

        else:
            print(serialized_record.errors)
            return JsonResponse({'statusCode':304,'msg':'Form Error',})

    except:
        return JsonResponse({'statusCode':500,'msg':'Something Went Wrong..',})

