from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class TestModel(models.Model):
    name = models.CharField(max_length=255)
    phone_number = PhoneNumberField()