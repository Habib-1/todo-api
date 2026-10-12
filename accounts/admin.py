from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

class UserAdmin(BaseUserAdmin):
    ordering=['email']
    list_display=['email','first_name','last_name','is_staff','is_superuser']
    search_fields=['email',]
    fieldsets=(
        (None,{'fields':('email','password')}),
        ("Personal Information" , {"fields":('first_name','last_name')}),
        ("Permission",{"fields":("is_staff","is_superuser")}),
    )
    add_fieldsets=(
        (None,{
            "classes": ("wide",),
            'fields':('email','password1','password2')}),
        ("Personal Info", {"classes": ("wide", "collapse"),"fields": ("first_name", "last_name")}),
    )


admin.site.register(CustomUser,UserAdmin)