# Generated by Django 2.2.4 on 2021-01-15 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20210114_1833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='users',
            name='last_name',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
    ]