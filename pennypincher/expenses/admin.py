from django.contrib import admin
from expenses.models import Category, Expense
# Register your models here.

admin.site.register(Expense)
admin.site.register(Category)