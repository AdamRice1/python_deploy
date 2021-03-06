# Generated by Django 2.2.4 on 2019-08-28 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0009_auto_20190828_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retirement',
            name='asset_one',
            field=models.CharField(default='Cash', max_length=45),
        ),
        migrations.AlterField(
            model_name='retirement',
            name='asset_one_percentage',
            field=models.IntegerField(default=20),
        ),
        migrations.AlterField(
            model_name='retirement',
            name='asset_three',
            field=models.CharField(default='Real Estate', max_length=45),
        ),
        migrations.AlterField(
            model_name='retirement',
            name='asset_three_percentage',
            field=models.IntegerField(default=60),
        ),
        migrations.AlterField(
            model_name='retirement',
            name='asset_two',
            field=models.CharField(default='Stocks', max_length=45),
        ),
        migrations.AlterField(
            model_name='retirement',
            name='asset_two_percentage',
            field=models.IntegerField(default=20),
        ),
    ]
