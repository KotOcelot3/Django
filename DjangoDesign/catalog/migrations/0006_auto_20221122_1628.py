# Generated by Django 3.2.16 on 2022-11-22 09:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20221122_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='Эскиз', error_messages={'unique': 'Такая категория уже существует!'}, help_text='Категории', max_length=30, unique=True, verbose_name='Категории'),
        ),
        migrations.AlterField(
            model_name='design',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 11, 22, 16, 28, 58, 433406), null=True, verbose_name='Дата'),
        ),
    ]
