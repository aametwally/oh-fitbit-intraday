# Generated by Django 2.1.3 on 2018-12-13 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20181017_2126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='oh_member',
        ),
        migrations.DeleteModel(
            name='Data',
        ),
    ]
