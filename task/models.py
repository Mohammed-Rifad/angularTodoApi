from django.db import models
from user.models import User
# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    description = models.CharField(max_length=200)
    date=models.CharField(max_length=20, default="")
    priority = models.CharField(max_length = 20, default = 'high')
    completion_date = models.CharField(max_length=20,default="not compleate")
    status = models.CharField(max_length=10,default="pending")
   
    class Meta:
      db_table = 'task_tb'