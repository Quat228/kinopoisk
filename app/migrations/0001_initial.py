# Generated by Django 4.2 on 2023-04-30 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('url', models.URLField()),
                ('preview_url', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=55)),
                ('profession', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('backdrop', models.URLField()),
                ('movie_length', models.IntegerField()),
                ('type', models.CharField(max_length=30)),
                ('name', models.CharField()),
                ('description', models.TextField()),
                ('premiere', models.DateTimeField()),
                ('slogan', models.CharField()),
                ('year', models.IntegerField()),
                ('poster', models.URLField()),
                ('trailer_url', models.URLField()),
                ('age_rating', models.IntegerField(default=18)),
                ('top10', models.BooleanField(null=True)),
                ('top250', models.BooleanField(null=True)),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='app.budget')),
                ('companies', models.ManyToManyField(related_name='movies', to='app.company')),
                ('genres', models.ManyToManyField(related_name='movies', to='app.genre')),
                ('persons', models.ManyToManyField(related_name='movies', to='app.person')),
            ],
        ),
    ]