from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *
from django.db.models import Q

@api_view(['GET'])
def endpoints(request):
    data = ['advocates/', 'advocates/:username']
    return Response(data)

@api_view(['GET'])
def add_advocate(request):
    Advocate.objects.create(
        username = request.GET 
    )
    return Response('added')

@api_view(['GET', 'POST'])
def advocate_list(request):
    if request.method == 'GET':

        query = request.GET.get('q') 
        if query == None:
            query = ''

        advocates = Advocate.objects.filter(Q(username__contains=query) | Q(bio__contains=query))
        serializer = AdvocateSerializer(advocates, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        advocate = Advocate.objects.create(
            username = request.data['username'],
            bio = request.data['bio']
        )
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

# @api_view(['GET', 'PUT', 'DELETE'])
# def advocate_details(request, username):
    
#     advocate = Advocate.objects.get(username=username)
    
#     if request.method == 'GET':
#         serializer = AdvocateSerializer(advocate, many=False)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         advocate.username = request.data['username']
#         advocate.bio = request.data['bio']
#         advocate.save()

#     elif request.method == 'DELETE':
#         advocate.delete()
#         return Response("usr was deleted")

class AdvocateDetail(APIView):
    def get(self, request, username):
        advocate = Advocate.objects.get(username=username)
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)
    
    def put(self, request, username):
        advocate = Advocate.objects.get(username=username)
        advocate.username = request.data['username']
        advocate.bio = request.data['bio']
        advocate.save()

        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

    def delete(self, request, username):
        advocate = Advocate.objects.get(username=username)
        advocate.delete()
        return Response('user was deleted. ')
    
@api_view(['GET'])
def companies_list(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)