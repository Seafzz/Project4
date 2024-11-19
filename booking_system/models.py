from django.db import models

# Create your models here.

class booking(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    appointment_date = models.DateField()
