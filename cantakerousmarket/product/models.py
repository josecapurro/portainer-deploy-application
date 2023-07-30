from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=130)
    description = models.CharField(max_length=130)
    active = models.BooleanField(default=False)

