from django.db import models
from authentication.models import User

# Create your models here.

#create Note Table in the database together with the attributes
class Note(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, default="")
    
    def __str__(self):
        return self.title[0:50]