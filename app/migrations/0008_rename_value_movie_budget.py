# Generated by Django 4.2 on 2023-05-01 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_currency_remove_movie_budget_delete_budget_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='value',
            new_name='budget',
        ),
    ]
