# Generated by Django 3.1.2 on 2020-10-10 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infomodel',
            old_name='first_name',
            new_name='f_name',
        ),
        migrations.RenameField(
            model_name='infomodel',
            old_name='last_name',
            new_name='l_name',
        ),
        migrations.AlterField(
            model_name='infomodel',
            name='selection',
            field=models.CharField(choices=[('OPTION0', 'Option 0'), ('OPTION1', 'Option 1'), ('OPTION2', 'Option 2')], max_length=50),
        ),
    ]
