# Generated by Django 4.2.5 on 2023-09-14 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Nacionality',
            new_name='Nationality',
        ),
        migrations.RenameField(
            model_name='nationality',
            old_name='nacionality',
            new_name='nationality',
        ),
    ]