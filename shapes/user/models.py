from django.db import models

# Create your models here.
class User(models.Model):

    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
    class Meta:
        db_table = "auth_user"

class Shape(models.Model):

    name = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    perimeter = models.CharField(max_length=50)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    class Meta:
        db_table = "shape"
