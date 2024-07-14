from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name}"
    
class Phone(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media/Phone", blank=True, null=True)
    price = models.IntegerField()



class Laptop(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media/Laptop", blank=True, null=True)
    price = models.IntegerField()


    
class Accessories(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media/Accessories", blank=True, null=True)
    price = models.IntegerField()

class Pokupka(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE, null=True, blank=True)
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, null=True, blank=True)
    accessory = models.ForeignKey(Accessories, on_delete=models.CASCADE, null=True, blank=True)
    pokupka_date = models.DateTimeField()

    def __str__(self):
        return f'{self.user.username} - {self.phone} - {self.laptop} - {self.accessory}'