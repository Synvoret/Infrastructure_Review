# Generated by Django 4.1.4 on 2023-01-04 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0016_alter_tour_bat11_temp_alter_tour_bat11_weekly_tpf_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='bswok_charger',
            field=models.CharField(default='Zielone', max_length=300),
        ),
        migrations.AlterField(
            model_name='tour',
            name='mains_charge',
            field=models.CharField(default='Zielone', max_length=300),
        ),
    ]