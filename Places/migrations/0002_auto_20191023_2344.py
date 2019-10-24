# Generated by Django 2.2.1 on 2019-10-23 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Places', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='places',
            name='Image',
        ),
        migrations.RemoveField(
            model_name='places',
            name='Title',
        ),
        migrations.AddField(
            model_name='places',
            name='Address',
            field=models.CharField(default='بدون آدرس ', max_length=102),
        ),
        migrations.AddField(
            model_name='places',
            name='Average',
            field=models.CharField(default='0', max_length=102),
        ),
        migrations.AddField(
            model_name='places',
            name='City',
            field=models.CharField(default='بدون شهر', max_length=102),
        ),
        migrations.AddField(
            model_name='places',
            name='Hardness',
            field=models.CharField(default='بدون درجه ی سختی', max_length=102),
        ),
        migrations.AddField(
            model_name='places',
            name='Likes',
            field=models.CharField(default='0', max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='places',
            name='Time',
            field=models.CharField(default='بدون  تخمین زمان ', max_length=102),
        ),
        migrations.AddField(
            model_name='places',
            name='categories',
            field=models.CharField(choices=[('Historical', 'Historical'), ('museums', 'museums'), ('Forests', 'Forests'), ('Public art', 'Public art'), ('national parks', 'national parks')], default='museums', max_length=200),
        ),
        migrations.AddField(
            model_name='places',
            name='title',
            field=models.CharField(default='بدون عنوان', max_length=102),
        ),
        migrations.AlterField(
            model_name='places',
            name='Description',
            field=models.TextField(default='بدون توضیحات'),
        ),
        migrations.CreateModel(
            name='PlaceImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, upload_to='')),
                ('places', models.ManyToManyField(to='Places.Places')),
            ],
        ),
    ]
