# Generated by Django 2.1.7 on 2019-02-23 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startuprank', '0007_auto_20190219_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='startup',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='user',
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
