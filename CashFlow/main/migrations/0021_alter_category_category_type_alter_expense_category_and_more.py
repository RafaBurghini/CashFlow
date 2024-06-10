# Generated by Django 5.0.3 on 2024-05-16 08:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_category_category_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_type',
            field=models.CharField(choices=[('I', 'Incomes'), ('E', 'Expenses'), ('G', 'Goals')], max_length=1),
        ),
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='goals',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='goals',
            name='start_date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name=datetime.date(2024, 5, 16)),
        ),
        migrations.AlterField(
            model_name='income',
            name='category',
            field=models.CharField(max_length=20),
        ),
    ]