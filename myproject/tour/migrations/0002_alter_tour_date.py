# Generated by Django 4.1.3 on 2022-12-11 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='date',
            field=models.DateField(),
        ),
    ]
