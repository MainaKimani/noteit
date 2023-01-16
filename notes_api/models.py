from django.db import models

# Create your models here.

#create Note Table in the database together with the attributes
class Note(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField(null=False, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title[0:50]