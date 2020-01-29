from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TodoSerializer, UserDetailSerializer
from .models import Todo
from django.contrib.auth import get_user_model
# Create your views here.

@api_view(['POST'])
def todo_create(request):
    serializer = TodoSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def todo_update_delete(request, todo_id):
    print('####')
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'PUT':
        serializer = TodoSerializer(instance=todo, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    if request.method == 'DELETE':
        print('######')
        todo.delete()
        
        return Response(status=204)



@api_view(['GET'])
def user_detail(request, user_id):
    user = get_object_or_404(get_user_model(), pk=user_id)
    serializer = UserDetailSerializer(instance=user)
    return Response(serializer.data)

