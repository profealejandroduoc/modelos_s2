# Generated by Django 5.0.6 on 2024-05-28 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_orm', '0005_alter_persona_f_nacto'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='sexo',
            field=models.CharField(default='O', max_length=1),
        ),
    ]