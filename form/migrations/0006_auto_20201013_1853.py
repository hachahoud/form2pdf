# Generated by Django 3.1.2 on 2020-10-13 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0005_auto_20201013_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infomodel',
            name='selection',
            field=models.CharField(choices=[(False, ''), ('OPTION0', 'Option 0'), ('OPTION1', 'Option 1'), ('OPTION2', 'Option 2')], max_length=50),
        ),
    ]