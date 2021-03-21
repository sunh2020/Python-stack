# Generated by Django 2.2.4 on 2021-01-15 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='email',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='name',
            field=models.CharField(default='', max_length=45),
            preserve_default=False,
        ),
    ]
