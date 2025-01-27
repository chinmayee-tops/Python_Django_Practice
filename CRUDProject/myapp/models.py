from django.db import models

# Create your models here.

class userinfo(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    city=models.CharField(max_length=20)