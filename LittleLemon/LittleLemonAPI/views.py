from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def menu_items(request):
    if request.method == 'GET':
        return Response('Menu Items', status=status.HTTP_200_OK)
    if request.method == 'POST':
        return Response('Menu Items', status=status.HTTP_201_CREATED)
    if request.method == 'PUT':
        return Response('Menu Items', status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        return Response('Menu Items', status=status.HTTP_204_NO_CONTENT)
