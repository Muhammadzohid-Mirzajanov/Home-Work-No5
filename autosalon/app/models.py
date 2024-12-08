from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    headquarters = models.CharField(max_length=150)
    established_year = models.IntegerField()

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.PositiveIntegerField()  # Bu yerga year qo'shildi

    def __str__(self):
        return self.name
