from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets,status
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.template.context_processors import request
from .serializers import ToDoSerializer
from .models import Todo
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response

# class TodoViewSet(viewsets.ModelViewSet):
#     permission_classes=[IsAuthenticated]
#     serializer_class = ToDoSerializer
#     filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
#     filterset_fields=['priority','status']
#     search_fields=['title','description']
#     ordering_fields=['created_at','updated_at'] 
#     ordering=['created_at']

#     def get_queryset(self):
#         return Todo.objects.filter(user=self.request.user)

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)



#Function Based View(FBV)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def todos_list_create_view(request):

    if request.method == "GET":
        todos=Todo.objects.filter(user=request.user)
        serializer=ToDoSerializer(todos,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        serializer=ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







@api_view(['GET','PUT','PATCH','DELETE'])
@permission_classes([IsAuthenticated])
def todos_retrieve_create_update_view(request,pk):

    todo=get_object_or_404(Todo,pk=pk,user=request.user)

    if request.method == "GET" :
        serializer=ToDoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method in ['PUT','PATCH'] :

        serializer=ToDoSerializer(todo,data=request.data,partial=request.method == "PATCH")
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
                
                

        
    