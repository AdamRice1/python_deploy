# Generated by Django 2.2.4 on 2019-08-27 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_businesses_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesses',
            name='listing',
            field=models.CharField(default='NYSE', max_length=25),
        ),
        migrations.AddField(
            model_name='businesses',
            name='stock_code',
            field=models.CharField(default='NYSE', max_length=25),
        ),
    ]
