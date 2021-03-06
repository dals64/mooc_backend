# Generated by Django 2.2.12 on 2021-01-28 23:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CatQuestion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('contenu', models.CharField(max_length=10000)),
                ('ressource', models.FileField(upload_to='Ressources')),
            ],
        ),
        migrations.CreateModel(
            name='Domaine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('libellé', models.CharField(max_length=50)),
                ('reponse', models.CharField(max_length=50)),
                ('libellé_reponse', models.CharField(max_length=200)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tuteur.CatQuestion')),
                ('cours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tuteur.Cours')),
                ('domaine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tuteur.Domaine')),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('niveau_social', models.CharField(max_length=50)),
                ('sexe', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('connaissance', models.ManyToManyField(to='Tuteur.Domaine')),
                ('cours', models.ManyToManyField(to='Tuteur.Cours')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cours',
            name='domaine',
            field=models.ManyToManyField(to='Tuteur.Domaine'),
        ),
    ]
