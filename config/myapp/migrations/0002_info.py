# Generated by Django 4.2.4 on 2023-08-21 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('roll', models.IntegerField()),
                ('phone', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=16)),
                ('texarea', models.TextField()),
                ('checkbox', models.CharField(max_length=20)),
                ('payment', models.DecimalField(decimal_places=2, max_digits=6)),
                ('django', models.BooleanField()),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
