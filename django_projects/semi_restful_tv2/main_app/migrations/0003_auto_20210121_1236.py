# Generated by Django 2.2.4 on 2021-01-21 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20210121_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='creator',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
