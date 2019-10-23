# Generated by Django 2.2.4 on 2019-08-28 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0007_retirement'),
    ]

    operations = [
        migrations.AddField(
            model_name='retirement',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, related_name='user_retire', to='user_app.Users'),
            preserve_default=False,
        ),
    ]
