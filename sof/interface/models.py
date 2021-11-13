from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
from django.db.models.base import Model
from django.utils import timezone

class Forum_query(models.Model):
    username=models.CharField(max_length=50)
    query=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    query_id=models.TextField(default="0000000000")
    
class Reply(models.Model):
    reply=models.TextField()
    reply_id=models.TextField(default="0000000000")