# Generated by Django 4.2 on 2023-05-07 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_profile_image'),
        ('app', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='film_work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app.filmwork'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='accounts.profile'),
        ),
    ]
