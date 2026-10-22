from django.urls import path, include
# from .views import TodoViewSet
# from rest_framework.routers import DefaultRouter
from .views import todos_list_create_view,todos_retrieve_create_update_view

# router = DefaultRouter()
# router.register('todos', TodoViewSet, basename='todo')

urlpatterns = [
    # path('', include(router.urls)),
    path('todos/',todos_list_create_view,name='list_create_view'),
    path('todos/<int:pk>/',todos_retrieve_create_update_view,name="retrieve_create_update_view"),
]