# Generated by Django 2.2.4 on 2021-01-18 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.CharField(default='notes', max_length=255),
            preserve_default=False,
        ),
    ]