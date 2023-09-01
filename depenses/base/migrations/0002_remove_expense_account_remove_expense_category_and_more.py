# Generated by Django 4.2.4 on 2023-09-01 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='account',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='category',
        ),
        migrations.RemoveField(
            model_name='income',
            name='account',
        ),
        migrations.RemoveField(
            model_name='income',
            name='category',
        ),
        migrations.RemoveField(
            model_name='transfer',
            name='fm',
        ),
        migrations.RemoveField(
            model_name='transfer',
            name='to',
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.DeleteModel(
            name='Expense',
        ),
        migrations.DeleteModel(
            name='Income',
        ),
        migrations.DeleteModel(
            name='nCategory',
        ),
        migrations.DeleteModel(
            name='Transfer',
        ),
        migrations.DeleteModel(
            name='xCategory',
        ),
    ]
