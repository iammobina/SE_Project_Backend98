# Generated by Django 2.1.2 on 2019-11-06 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
        ('Places', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='places',
            name='leader',
            field=models.ManyToManyField(to='Users.Leader'),
        ),
    ]