# Generated by Django 4.2.5 on 2023-09-14 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_rename_nacionality_nationality_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='athletes',
            old_name='nacionality',
            new_name='nationality',
        ),
    ]
