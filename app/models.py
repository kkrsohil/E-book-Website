from django.db import models

# Create your models here.

class contact_details(models.Model):
    user_name= models.CharField(max_length=155)
    user_email= models.EmailField()
    message=models.TextField(max_length=1055)
    def __str__(self):
        return self.user_name

class blog_details(models.Model):
    user_name= models.CharField(max_length=155)
    blog_msg=models.TextField()
    blog_link= models.CharField(max_length=155)
    def __str__(self):
        return self.user_name

    
    