from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny
from .serializers import ToDoSerializer
from .models import Todo

class TodoViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    serializer_class = ToDoSerializer

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

        
    