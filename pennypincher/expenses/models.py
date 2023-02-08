from django.db import models
from colorfield.fields import ColorField


class Category(models.Model):
    name = models.CharField(max_length=100)
    color = ColorField(default="#FF0000")

    def __str__(self):
        return self.name


class Expense(models.Model):
    CURRENCIES = (("usd", "$"), ("eur", "€"), ("pln", "PLN"))
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL
    )
    currency = models.CharField(max_length=200, choices=CURRENCIES)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
