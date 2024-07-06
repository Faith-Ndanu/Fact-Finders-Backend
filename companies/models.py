from django.db import models

# Create your models here.

class Company(models.Model):
    first_name=models.CharField(max_length=20)
    company_email = models.EmailField()
    donor_id=models.IntegerField()
    company_id=models.IntegerField()
    password=models.CharField(max_length=20)
    confirm_password=models.CharField(max_length=20)

    def __str__(self):
         return f"{self.first_name} {self.company_id}"
