# Generated by Django 3.1.6 on 2021-03-14 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_auto_20210302_0526'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='isInTheater',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='isTrending',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='isUpcoming',
            field=models.BooleanField(default=False),
        ),
    ]