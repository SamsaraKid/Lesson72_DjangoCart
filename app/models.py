from django.db import models
from django.contrib.auth.models import User


class Tovar(models.Model):
    opis = models.CharField(max_length=500)
    price = models.IntegerField()
    image = models.CharField(max_length=500)
    skidka = models.FloatField(default=1)

    def __str__(self):
        return self.opis


class Korzina(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    tovar = models.ForeignKey(Tovar, on_delete=models.CASCADE)
    count = models.IntegerField()
    summa = models.DecimalField(decimal_places=2, max_digits=8)

    def calcSumma(self):
        return self.count * self.tovar.price * self.tovar.skidka


class Zakaz(models.Model):
    address = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    total = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True)


class Zacazitems(models.Model):
    tovar = models.ForeignKey(Tovar, on_delete=models.CASCADE)
    count = models.IntegerField()
    zakaz = models.ForeignKey(Zakaz, on_delete=models.CASCADE)


class Favorites(models.Model):
    tovar = models.ForeignKey(Tovar, on_delete=models.CASCADE)

