# Generated by Django 3.1.2 on 2020-10-04 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='event_choice',
            field=models.BooleanField(),
        ),
    ]
