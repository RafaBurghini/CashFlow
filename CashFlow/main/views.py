from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth import logout, get_user_model 
from .models import Income, Expense, Transaction, Goals
from .forms import IncomeForm, ExpenseForm, RegisterForm, GoalForm, GoalAddAmountForm
from django.http import HttpResponse
from django.db.models import Sum
import csv
from datetime import date
from social_core.pipeline.partial import partial
import matplotlib as plt
import io
import urllib, base64
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# AUTHENTICATION VIEWS

def home(request):
    return render(request, 'home.html')

@partial
# This function is used to require the user to enter an email address when they sign up with a social account
def require_email(strategy, details, user=None, is_new=False, *args, **kwargs):
    if user and user.email:
        return
    elif is_new and not details.get('email'):
        email = strategy.request_data().get('email')
        if email:
            details['email'] = email
        else:
            return strategy.redirect('/require_email')

# This function is used to require the user to enter an email address when they sign up 
def sign_up(request):
    if request.method == 'POST':
        form= RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'registration/sign_up.html', {'form': form})


def profile(request):
    return render(request, 'profile.html') 

def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
# This function is used to delete the user account
def delete_account(request):
    user = get_user_model().objects.get(pk=request.user.pk)
    user.delete()
    return redirect('home')


# CASHFLOW VIEWS

def add_income(request):
    # This function is used to add a new expense record
    if request.method == 'POST':
        form = IncomeForm(request.POST, request.user)
        # This validate the form
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            # This create a new transaction record
            Transaction.objects.create(
                user=request.user,
                amount=income.amount,
                title=income.title,
                date=income.date,
                notes=income.notes
            )
            return redirect('incomes')
    else:
        # This create a new form
        form = IncomeForm()
    # This render the expenses.html template with the form and all the transactions
    return render(request, 'incomes.html', {'form': form})


def add_expense(request):
    # This function is used to add a new expense record
    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.user)
        # This validate the form
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            # This create a new transaction record
            Transaction.objects.create(
                user=request.user,
                amount=expense.amount,
                title=expense.title,
                date=expense.date,
                notes=expense.notes
            )
            return redirect('expenses')
    else:
        # This create a new form
        form = ExpenseForm()
    # This render the expenses.html template with the form and all the transactions
    return render(request, 'expenses.html', {'form': form})



# DASHBOARD VIEW

def dashboard(request):
    today = timezone.now().date()
    # This get all the transactions for the user and order them by date
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    # This calculate the total income, total expense, and balance
    total_income = round(Income.objects.filter(user=request.user).aggregate(Sum('amount'))['amount__sum'] or 0,1)
    total_expense = round(Expense.objects.filter(user=request.user).aggregate(Sum('amount'))['amount__sum'] or 0,1)
    balance = total_income - total_expense
    # This create the forms for income, expense, and goals
    income_form = IncomeForm()
    expense_form = ExpenseForm()
    goal_form = GoalForm()
    # This get all the goals for the user
    goals = Goals.objects.filter(user=request.user)
    goals_in_progress = Goals.objects.filter(user=request.user, is_completed=False)
    # This calculate the progress of the goals
    for goal in goals_in_progress:
        goal.progress = round((goal.current_amount / goal.target_amount) * 100 if goal.target_amount else 0)
    
    # This render the dashboard.html template with all the data
    return render(request, 'dashboard.html', {'total_income': total_income, 
                                            'total_expense': total_expense, 
                                            'transactions': transactions, 
                                            'balance': balance, 
                                            'goals': goals, 
                                            'today': today, 
                                            'income_form': income_form, 
                                            'expense_form': expense_form, 
                                            'goal_form': goal_form, 
                                            'goals_in_progress': goals_in_progress,})


# GOALS VIEWS

def goals(request):
    # This function is used to add a new goal record
    if request.method == 'POST':
        form = GoalForm(request.POST, request.user)
        if form.is_valid():
            # This save the form
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('goals')
    else:
        # This create a new form
        form = GoalForm()
    # This get all the goals for the user
    goals = Goals.objects.filter(user=request.user)
    completed_goals = Goals.objects.filter(user=request.user, is_completed=True)
    goals_in_progress = Goals.objects.filter(user=request.user, is_completed=False)
    # This calculate the progress of the goals in progress
    for goal in goals_in_progress:
         goal.progress = round((goal.current_amount / goal.target_amount) * 100 if goal.target_amount else 0)
    
    # This render the goals.html template with the form and all the goals
    return render(request, 'goals.html', {'form': form, 'goals': goals, 'completed_goals': completed_goals, 'goals_in_progress': goals_in_progress})


def complete_goal(request, goal_id):
    # This function is used to complete a goal record
    goal = Goals.objects.get(id=goal_id)
    goal.is_completed = True
    goal.save()
    return redirect('goals')


def edit_goal(request, goal_id):
    # This function is used to edit a goal record
    goal = get_object_or_404(Goals, id=goal_id)
    # This calculate the progress of the goal
    goal.progress = round((goal.current_amount / goal.target_amount) * 100 if goal.target_amount else 0)
    # This validate the form
    if request.method == 'POST':
        form = GoalAddAmountForm(request.POST)
        if form.is_valid():
            # This add the current amount to the goal
            current_amount = form.cleaned_data.get('current_amount')
            goal.current_amount += current_amount
            goal.save()
            return redirect('edit_goal', goal_id)
    else:
        form = GoalAddAmountForm()
    return render(request, 'edit_goal.html', {'form': form, 'goal': goal})


def delete_goal(request, goal_id):
    goal = Goals.objects.get(id=goal_id)
    goal.delete()
    return redirect('dashboard')


# DOWNLOAD VIEWS

def download_transactions(request):
    # Create an http response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="transactions.csv"'

    # Create the csv writer
    writer = csv.writer(response)

    # write the header
    writer.writerow(['Date', 'Category', 'Amount', 'Type', 'Notes', 'Title'])

    # write the transactions for incomes
    for income in Income.objects.all():
        writer.writerow([income.date, income.category, income.amount, 'Income', income.notes, income.title])

    # write the transactions for expenses
    for expense in Expense.objects.all():
        writer.writerow([expense.date, expense.category, expense.amount, 'Expense', expense.notes, expense.title])

    return response



