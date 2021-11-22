from django.db import models

# Create your models here.

class JobCart(models.Model): 
    fullname = models.CharField(max_length=200, null=True)
    id_no = models.CharField(max_length=200, null=True)
    job_type = models.CharField(max_length=13, null=True)
    job_description = models.TextField(max_length=500, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    

