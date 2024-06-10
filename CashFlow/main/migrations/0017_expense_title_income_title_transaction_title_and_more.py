# Generated by Django 5.0.3 on 2024-05-11 09:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_transaction_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='title',
            field=models.CharField(default='Expense', max_length=30),
        ),
        migrations.AddField(
            model_name='income',
            name='title',
            field=models.CharField(default='Income', max_length=30),
        ),
        migrations.AddField(
            model_name='transaction',
            name='title',
            field=models.CharField(default='Transaction', max_length=30),
        ),
        migrations.AlterField(
            model_name='goals',
            name='start_date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name=datetime.date(2024, 5, 11)),
        ),
    ]