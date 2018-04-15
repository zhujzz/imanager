from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=36)
    email = models.CharField(max_length=128, null=True)
    create_at = models.DateTimeField('create time')
