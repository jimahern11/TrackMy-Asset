# Generated by Django 2.2.6 on 2020-04-20 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips_app', '0008_auto_20200420_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locations',
            name='done',
        ),
    ]