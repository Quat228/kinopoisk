# Generated by Django 4.2 on 2023-04-30 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='companies',
        ),
        migrations.AlterField(
            model_name='rating',
            name='rate',
            field=models.FloatField(),
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]
