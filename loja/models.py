from django.db import models

class Shirt(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=7)
    new = models.BooleanField()

    def __str__(self):
        return self.name
    
