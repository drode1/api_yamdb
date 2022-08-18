# Generated by Django 2.2.16 on 2022-08-18 13:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0002_auto_20220813_0718'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('-date_joined', 'username'),
                     'verbose_name': 'Пользователь',
                     'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.PositiveIntegerField(blank=True, null=True,
                                              validators=[
                                                  django.core.validators.MinValueValidator(
                                                      10000),
                                                  django.core.validators.MaxValueValidator(
                                                      99999)],
                                              verbose_name='Код подтверждения'),
        ),
    ]