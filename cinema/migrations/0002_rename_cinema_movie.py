# Generated by Django 4.0.4 on 2022-04-30 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cinema',
            new_name='Movie',
        ),
    ]
