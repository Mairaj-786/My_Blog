# Generated by Django 3.0.8 on 2020-10-11 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.TextField(max_length=220)),
                ('message', models.TextField(max_length=400)),
            ],
        ),
    ]
