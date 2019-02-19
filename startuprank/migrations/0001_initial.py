# Generated by Django 2.1.7 on 2019-02-17 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField(default='')),
                ('review_date', models.DateTimeField(verbose_name='review date')),
            ],
        ),
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('estab_year', models.IntegerField(default=2000, verbose_name='year established')),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='startup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startuprank.Startup'),
        ),
    ]
