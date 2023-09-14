from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def menu_items(request):
    if request.method == 'GET':
        return Response('Fetch All Menu Items', status=status.HTTP_200_OK)
    if request.method == 'POST':
        return Response('Menu Item Posted Successfully', status=status.HTTP_201_CREATED)
    if request.method == 'PUT':
        return Response('Menu Item has been Updated', status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        return Response('Menu Item has been Deleted', status=status.HTTP_204_NO_CONTENT)
