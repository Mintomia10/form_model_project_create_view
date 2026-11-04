from django.db import models

# Create your models here.
class StudentModel(models.Model):
    
    st_id = models.CharField(max_length=100)
    
    st_name = models.CharField(max_length=100)
    
    st_email = models.EmailField()
    
    st_dept = models.CharField(max_length=100)
    
    st_address = models.TextField()
    
    