# Generated by Django 3.0.3 on 2020-04-08 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_remove_movie_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]