# Generated by Django 3.1.6 on 2021-02-01 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tuteur', '0004_auto_20210129_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='propostion1',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='question',
            name='propostion2',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='question',
            name='propostion3',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='question',
            name='propostion4',
            field=models.CharField(default='', max_length=250),
        ),
    ]
