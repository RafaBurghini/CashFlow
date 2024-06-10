from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone

# model for income records
class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=1)
    title = models.CharField(max_length=30, blank=False, null=False, default='Income') 
    date = models.DateTimeField(default=timezone.now, auto_now=False, blank=True, null=True)
    notes=models.TextField(blank=True, null=True)

# model for expense records
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=1)
    title = models.CharField(max_length=30, blank=False, null=False, default='Expense') 
    date = models.DateTimeField(default=timezone.now, auto_now=False, blank=True, null=True)
    notes=models.TextField(blank=True, null=True)


# model for transactions records
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=1)
    title = models.CharField(max_length=30, blank=False, null=False, default='Transaction') 
    date = models.DateTimeField(null=True, blank=True)
    notes=models.TextField(blank=True, null=True)


# model for goals records
class Goals(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=10, decimal_places=1)
    current_amount = models.DecimalField(max_digits=10, decimal_places=1)
    start_date = models.DateField(date.today(), blank=True, null=True, auto_now_add=True, auto_now=False)
    desired_date = models.DateField(blank=True, null=True)
    notes=models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)


