# Generated by Django 2.2.4 on 2021-01-20 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_author_notes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='publishers',
            new_name='books',
        ),
    ]
