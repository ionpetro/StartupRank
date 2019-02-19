# Generated by Django 2.1.7 on 2019-02-19 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startuprank', '0006_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='num_vote_down',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='vote',
            name='num_vote_up',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='vote',
            name='vote_score',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]
