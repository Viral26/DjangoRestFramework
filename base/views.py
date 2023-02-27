from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

@api_view(['GET'])
def endpoints(request):
    data = ['advocates/', 'advocates/:username']
    return Response(data)

@api_view(['GET'])
def advocate_list(request):
    query = request.GET.get('q')
    print('------------------->', query)
    if query == None:
        query = ''

    advocates = Advocate.objects.filter(username__contains=query, bio__contains=query)
    serializer = AdvocateSerializer(advocates, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def advocate_details(request, username):
    advocate = Advocate.objects.get(username=username)
    serializer = AdvocateSerializer(advocate, many=False)
    return Response(serializer.data)