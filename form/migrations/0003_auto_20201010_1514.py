# Generated by Django 3.1.2 on 2020-10-10 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_auto_20201010_1512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infomodel',
            old_name='f_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='infomodel',
            old_name='l_name',
            new_name='last_name',
        ),
    ]
