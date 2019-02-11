# Generated by Django 2.0.7 on 2019-02-11 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=30)),
                ('message', models.TextField(max_length=500)),
                ('to', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
