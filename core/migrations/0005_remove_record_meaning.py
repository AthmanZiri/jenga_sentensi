# Generated by Django 3.2.5 on 2022-10-26 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20221026_0856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='meaning',
        ),
    ]
