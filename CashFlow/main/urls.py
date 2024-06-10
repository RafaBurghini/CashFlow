from django.urls import path
from . import views


urlpatterns = [
    # the following are the URLs for the home, sign_up, dashboard, and profile views
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile', views.profile, name='profile'),
    path('delete_account', views.delete_account, name='delete_account'),
    # the following are the URLs for the income, expense, and goal records
    path('incomes', views.add_income, name='incomes'),
    path('expenses', views.add_expense, name='expenses'),
    path('goals', views.goals, name='goals'),
    path('complete_goal/<int:goal_id>/', views.complete_goal, name='complete_goal'),
    path('edit_goal/<int:goal_id>/', views.edit_goal, name='edit_goal'),
    path('delete_goal', views.delete_goal, name='delete_goal'),

    # the following are the URLs for the transaction records
    path('download_transactions/', views.download_transactions, name='download_transactions'),
    # the following are the URLs for the categories

]