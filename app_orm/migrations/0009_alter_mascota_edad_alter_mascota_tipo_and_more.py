# Generated by Django 5.0.6 on 2024-05-28 19:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_orm', '0008_alter_persona_sexo_mascota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='edad',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(300)]),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='tipo',
            field=models.CharField(choices=[('Manatí', 'Manatí'), ('Gato', 'Gato'), ('Perro', 'Perro'), ('Anaconda', 'Anaconda')], max_length=30),
        ),
        migrations.AlterField(
            model_name='persona',
            name='sexo',
            field=models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino'), ('O', 'Otro')], default='O', max_length=1),
        ),
    ]