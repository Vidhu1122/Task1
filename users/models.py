from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name