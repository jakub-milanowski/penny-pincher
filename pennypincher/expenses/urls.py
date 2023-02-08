from expenses import views
from django.urls import path

urlpatterns = [
    path("", views.expenses, name="expenses"),
    path("expense/<int:pk>/", views.expense, name="expense"),
    path("create-expense/", views.createExpense, name="create-expense"),
    path("edit-expense/<int:pk>/", views.editExpense, name="edit-expense"),
    path("delete-expense/<int:pk>/", views.deleteExpense, name="delete-expense"),
]
