# Generated by Django 3.2.1 on 2021-06-05 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0014_alter_user_csvs_archivocsv'),
    ]

    operations = [
        migrations.AddField(
            model_name='medidas',
            name='rssi_dbm',
            field=models.CharField(default=10, max_length=200),
            preserve_default=False,
        ),
    ]
