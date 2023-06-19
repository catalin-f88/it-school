from django.db import models
 
# Create your models here.
class UserForm(models.Model):  
    firstname = models.CharField("Enter first name", max_length = 50)  
    lastname  = models.CharField("Enter last name", max_length = 50)  
    email     = models.EmailField("Enter Email")  
    file      = models.FileField(upload_to="cache")
    message   = models.CharField("Enter your secret message", max_length=100, default="")
   
    class Meta:  
        db_table = "users"