# Generated by Django 4.0.3 on 2023-02-23 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='movies.category'),
        ),
    ]