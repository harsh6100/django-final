from django.db import models

class Account(models.Model):
    
    email=models.CharField(max_length=30)
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)

    def __str__(self):
        return self.email