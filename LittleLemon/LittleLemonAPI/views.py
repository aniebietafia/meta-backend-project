from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


# Create your views here.


'''
Setup GET and POST methods for menu-items. Handle GET requests from the database with filtering,
ordering, and pagination. Implement search functionality. Handle POST requests with validation
and saving to the database.
'''


@api_view(['GET', 'POST'])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.all()
        # items = MenuItem.objects.select_related('category').all()
        to_price = request.query_params.get('to_price')
        category_name = request.query_params.get('category')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')
        perpage = request.query_params.get('perpage', default=5)
        page = request.query_params.get('page', default=1)

        if category_name:
            items = items.filter(category__title=category_name)
        if to_price:
            items = items.filter(price=to_price)
        if search:
            items = items.filter(title__icontains=search)
        if ordering:
            ordering_fields = ordering.split(",")
            items = items.order_by(*ordering_fields)

        paginator = Paginator(items, per_page=perpage)
        try:
            items = paginator.page(number=page)
        except EmptyPage:
            items = []
        serialized_item = MenuItemSerializer(items, many=True)
        return Response(serialized_item.data)
    if request.method == 'POST':
        serialized_item = MenuItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED)


'''
Setup GET, PUT, and DELETE methods for a single menu-item. Handle GET requests from the database.
Handle PUT requests with validation and saving to the database. Handle DELETE requests by deleting
the menu-item from the database.
'''


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def menu_item(request, pk):
    item = get_object_or_404(MenuItem, pk=pk)
    if request.method == 'GET':
        serialized_item = MenuItemSerializer(item)
        return Response(serialized_item.data)
    if request.method == 'PUT':
        serialized_item = MenuItemSerializer(item, data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data)
    if request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

