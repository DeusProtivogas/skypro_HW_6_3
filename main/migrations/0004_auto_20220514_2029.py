# Generated by Django 2.2.12 on 2022-05-14 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_location_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ad',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='user',
            name='location_id',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
