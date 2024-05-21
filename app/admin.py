from django.contrib import admin
from .models import contact_details,blog_details

# Register your models here.
@admin.register(contact_details)
class contact_detailsAdmin(admin.ModelAdmin):
    list_display=('id', 'user_name','user_email','message')
    
@admin.register(blog_details)
class blog_detailsAdmin(admin.ModelAdmin):
    list_display=('id','user_name','blog_msg','blog_link')