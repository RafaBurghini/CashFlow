from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Income, Expense, Goals
import datetime
from django.core.exceptions import ValidationError
from django.db.models import Q

# Form for registering a new user
class RegisterForm (UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['first_name','username', 'email','password1', 'password2']

    

# form for new incomes
class IncomeForm(forms.ModelForm):

    # personalization of the form

    amount = forms.DecimalField(widget=forms.TextInput(attrs={'placeholder': '0.00'}), required=True)
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Income'}), required=True)

    # form fields
    class Meta:
        model = Income
        fields = ['amount', 'title', 'notes', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')
        }
    # validation for amount (cannot be negative)
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount is not None and amount < 0:
            raise ValidationError('Amount cannot be negative.')
        return amount


# form for new expenses
class ExpenseForm(forms.ModelForm):
    amount = forms.DecimalField(widget=forms.TextInput(attrs={'placeholder': '0.00'}), required=True)
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Expense'}), required=True)

    # form fields
    class Meta:
        model = Expense
        fields = ['amount', 'title','notes', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')
        }
    
    # validation for amount (cannot be negative)
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount is not None and amount < 0:
            raise ValidationError('Amount cannot be negative.')
        return amount



# form for new goals
class GoalForm(forms.ModelForm):

    # personalization of the form
    class Meta:
        model = Goals
        fields = ['target_amount', 'name','notes','current_amount','desired_date']
        widgets = {
            'goal_name': forms.TextInput(attrs={'placeholder': 'Name your goal'}),
            'desired_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    # validation for amount (cannot be negative)
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount is not None and amount < 0:
            raise ValidationError('Amount cannot be negative.')
        return amount


class GoalAddAmountForm(forms.ModelForm):
    # personalization of the form
    class Meta:
        model = Goals
        fields = ['current_amount']
        widgets = {
            'current_amount': forms.NumberInput(attrs={'placeholder': '0.00'})
        }
    def clean_current_amount(self):
        current_amount = self.cleaned_data.get('current_amount')
        if current_amount is not None and current_amount < 0:
            raise ValidationError('Amount cannot be negative.')
        return current_amount
    


