# Generated by Django 3.2.1 on 2021-06-21 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0025_alter_torre_measure_torre_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='torre',
            old_name='nombre',
            new_name='cell_id',
        ),
        migrations.AddField(
            model_name='torre',
            name='lac',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
