# Generated by Django 3.0.3 on 2020-04-07 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('summary', models.CharField(max_length=500)),
                ('director', models.CharField(max_length=50)),
                ('writer', models.CharField(max_length=50)),
                ('stars', models.CharField(max_length=50)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=10000)),
            ],
        ),
    ]