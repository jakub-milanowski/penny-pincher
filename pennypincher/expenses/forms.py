from django.forms import ModelForm
from django import forms
from expenses.models import Expense


class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ["name", "amount", "currency", "comment", "category"]

    def __init__(self, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})
