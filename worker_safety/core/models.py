from django.db import models
from django.core.validators import RegexValidator

class Worker(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    address=models.CharField(max_length=1000)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    medical_history=models.CharField(max_length=500)
    saftey_breach=models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name



# Create your models here.
