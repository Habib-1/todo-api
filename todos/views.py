from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny
from .serializers import ToDoSerializer
from .models import Todo
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class TodoViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    serializer_class = ToDoSerializer
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields=['priority','status']
    search_fields=['title','description']
    ordering_fields=['created_at','updated_at'] 
    ordering=['created_at']

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

        
    