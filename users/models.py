from django.db import models

# Create your models here.

class User(models.Model):
    username   = models.CharField(max_length = 200 , null = True)
    email      = models.EmailField(max_length=200 , null = True , unique=True)
    password   = models.CharField(max_length=200 , null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users"

