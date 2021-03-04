# Generated by Django 2.2.12 on 2021-01-29 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tuteur', '0002_auto_20210129_0007'),
    ]

    operations = [
        migrations.CreateModel(
            name='session_cours',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('progression', models.IntegerField()),
                ('note', models.IntegerField()),
                ('cours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tuteur.Cours')),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tuteur.Etudiant')),
            ],
        ),
    ]
