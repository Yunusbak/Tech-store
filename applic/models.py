from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100, blank=True)

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

