from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your models here.
PRIORITY=[
    ("Low","Low"),
    ("Medium","Medium"),
    ("High","High"),
]
STATUS=[
    ("Pending","Pending"),
    ("In Progress","In Progress"),
    ("Completed","Completed"),
    ("Cancelled","Cancelled"),
]

class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='todos')
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=500,blank=True)
    priority=models.CharField(max_length=30,choices=PRIORITY,default="Low")
    status=models.CharField(max_length=30,choices=STATUS,default="Pending")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title