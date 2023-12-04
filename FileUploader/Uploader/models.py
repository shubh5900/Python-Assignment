from django.db import models

# Create your models here.

Class Document(models.Model):
    File=models.FileField(storage=select_storage)

