from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from . models import User
from random import randint
from .serializers import UserSerializer

@api_view(['POST'])
def user_signup(request):
    try:
        params = request.data
        email = params['email']

        if not User.objects.filter(email = email).exists():
            serialized_set = UserSerializer(data = params)
            if serialized_set.is_valid():
                serialized_set.save()
                return JsonResponse({'statusCode': 201, 'message':'Signup Succesful'})            
            else:
                print(serialized_set.errors)
                return JsonResponse({'statusCode': 402,'message':'form error'})
        else:
            return JsonResponse({'statusCode':403,'message':'Email Already Exists'})    
    except:
            return JsonResponse({'statusCode': 500,'message': 'something went wrong'})


@api_view(['POST'])
def user_auth(request):  
    print("bxhjgcszdgvjhdfg")  
    try:       
        params = request.data 
        print(params)        
        try:             
            auth = User.objects.get(email = params['email'], password = params['password'])           
            token = 'user'+ str(randint(11111,99999))
            context = {
                'statusCode':200,
                'message':'Login Succesful',
                'token':token,
                'userId':auth.id,
                'userName':auth.name,
                }
            return JsonResponse(context)
        except Exception as e:             
            return JsonResponse({'statusCode':401,'message':'Invalid UserName or Password'})
    except Exception as e:        
        return JsonResponse({'statusCode':500,'message':'Something Went Wrong...'})


def check_email(request):
    email = request.GET['email']
    email_exist = User.objects.filter(email = email).exists()
    print(email_exist)
    if email_exist:
        return JsonResponse({'statusCode':202,})

    return JsonResponse({'statusCode':200,})
