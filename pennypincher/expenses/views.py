from django.shortcuts import render, redirect
from expenses.models import Expense, Category
from expenses.forms import ExpenseForm


def expenses(request):
    qs = Expense.objects.all().order_by("-date")
    context = {"expenses": qs}
    return render(request, "expenses/expenses.html", context)


def expense(request, pk):
    qs = Expense.objects.get(id=pk)
    context = {"expense": qs}
    return render(request, "expenses/expense.html", context)


def createExpense(request):
    form = ExpenseForm
    if request.method == "POST":
        form = ExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.save()
            return redirect("expenses")
    context = {"form": form}
    return render(request, "expenses/expense_form.html", context)


def editExpense(request, pk):
    expense = Expense.objects.get(id=pk)
    form = ExpenseForm(instance=expense)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect("expenses")
    context = {"form": form}
    return render(request, "expenses/expense_form.html", context)


def deleteExpense(request, pk):
    expense = Expense.objects.get(id=pk)
    if request.method == "POST":
        expense.delete()
        return redirect("expenses")
    context = {"expense": expense}
    return render(request, "expenses/delete_expense.html", context)
