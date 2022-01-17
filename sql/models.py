from django.db import models

# Create your models here.
class Todolist(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField(null=True, blank=True)
    birthday = models.TextField(null=True, blank=True)
    age = models.TextField(null=True, blank=True)
    gender = models.TextField(null=True, blank=True)
    date=models.TextField(null=True, blank=True)

class DeviceAll(models.Model):
    temp = models.FloatField(blank = True, null = True)
    spo2 = models.FloatField(blank = True, null = True)
    hr = models.FloatField(blank = True, null = True)
    create = models.DateTimeField(auto_now_add = True)
    
    