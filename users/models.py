from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
# This code defines a Django model for a User, with fields for full name, mobile number, email, and password.
# The mobile number and email fields are unique, ensuring no duplicates in the database.s