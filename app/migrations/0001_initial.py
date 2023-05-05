from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='FilmWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('backdrop', models.URLField()),
                ('movie_length', models.IntegerField()),
                ('type', models.CharField(max_length=30)),
                ('name', models.CharField()),
                ('description', models.TextField()),
                ('premiere', models.DateTimeField()),
                ('slogan', models.CharField(null=True)),
                ('year', models.IntegerField()),
                ('budget', models.IntegerField(default=0)),
                ('poster', models.URLField()),
                ('trailer_url', models.URLField()),
                ('age_rating', models.IntegerField(default=18)),
                ('top10', models.BooleanField(null=True)),
                ('top250', models.BooleanField(null=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='film_works', to='app.currency')),
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
                ('photo', models.URLField()),
                ('name', models.CharField(max_length=55)),
                ('profession', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('film_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='app.filmwork')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='accounts.profile')),
            ],
        ),
        migrations.AddField(
            model_name='filmwork',
            name='genres',
            field=models.ManyToManyField(related_name='film_works', to='app.genre'),
        ),
        migrations.AddField(
            model_name='filmwork',
            name='persons',
            field=models.ManyToManyField(related_name='film_works', to='app.person'),
        ),
    ]
