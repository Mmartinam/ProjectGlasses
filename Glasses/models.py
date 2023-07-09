
from django.db import models

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    owner = models.CharField(max_length=20)
    date = models.DateField()

    def __str__(self):
        return f"{self.name}"


class Glasses(models.Model):
    name = models.CharField(max_length=20)
    model = models.IntegerField()
    quantity = models.IntegerField()
    price = models.IntegerField()
    colorFrame = models.CharField(max_length=20)
    colorGlass = models.CharField(max_length=20)
    form = models.CharField(max_length=20)
    material = models.CharField(max_length=20)
    polarization = models.BooleanField()
    photo = models.ImageField(upload_to='images')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Client(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"


class Sales(models.Model):
    glasses = models.ForeignKey(Glasses, on_delete=models.CASCADE)
    date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.glasses}"


class Order(models.Model):
    glasses = models.ForeignKey(Glasses, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.glasses}"
    

