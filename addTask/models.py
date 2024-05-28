from django.db import models
from addCategory.models import addCategory
# Create your models here.
class addTask(models.Model):
    taskTitle=models.CharField(max_length=50)
    taskDescription=models.CharField(max_length=100)
    boolean=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now=False, auto_now_add=False)
    category=models.ManyToManyField(addCategory)


    def __str__(self) -> str:
        return self.taskTitle