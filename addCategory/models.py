from django.db import models

# Create your models here.
class addCategory(models.Model):
    category=models.CharField(max_length=50)



    def __str__(self) :
        return self.category