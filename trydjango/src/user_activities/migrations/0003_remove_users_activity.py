# Generated by Django 2.0.7 on 2020-06-25 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_activities', '0002_activityperiods_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='activity',
        ),
    ]