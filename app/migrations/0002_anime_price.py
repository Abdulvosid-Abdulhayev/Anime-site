# Generated by Django 5.1.1 on 2024-10-29 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
