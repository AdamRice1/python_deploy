# Generated by Django 2.2.4 on 2019-08-28 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0010_auto_20190828_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retirement',
            name='asset_one',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='retirement',
            name='asset_one_percentage',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='retirement',
            name='asset_three',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='retirement',
            name='asset_three_percentage',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='retirement',
            name='asset_two',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='retirement',
            name='asset_two_percentage',
            field=models.IntegerField(),
        ),
    ]