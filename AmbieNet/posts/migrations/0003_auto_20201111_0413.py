# Generated by Django 3.1.2 on 2020-11-11 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20201111_0340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='latitud',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='longitud',
            new_name='longitude',
        ),
    ]
