# Generated by Django 3.2.8 on 2022-05-16 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0032_rename_radio_torre_data_tecnologia'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_csvs',
            name='activated',
            field=models.BooleanField(default=True),
        ),
    ]