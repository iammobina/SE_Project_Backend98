# Generated by Django 2.1.2 on 2019-12-26 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
        ('Places', '0002_places_leader'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(default='بدون کامنت', max_length=100)),
                ('place', models.ManyToManyField(to='Places.Places')),
                ('user', models.ManyToManyField(to='Users.user')),
            ],
        ),
    ]