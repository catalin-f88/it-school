from django.db import models
 
# Create your models here.
class UserForm(models.Model):  
    name      = models.CharField("Enter your name", max_length = 50, default="")  
    file      = models.FileField(upload_to="cache")
    message   = models.CharField("Enter your secret message", max_length=100, default="")
   
    class Meta:  
        db_table = "users"