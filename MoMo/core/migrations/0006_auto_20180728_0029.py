# Generated by Django 2.0.7 on 2018-07-28 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180728_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saasinstance',
            name='address',
        ),
        migrations.RemoveField(
            model_name='saasinstance',
            name='hostname',
        ),
        migrations.AddField(
            model_name='saasinstance',
            name='url',
            field=models.URLField(default=''),
        ),
    ]