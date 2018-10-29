# Generated by Django 2.1.1 on 2018-10-29 20:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Naslov',
            fields=[
                ('ID_Pošta', models.AutoField(primary_key=True, serialize=False)),
                ('ime_pošta', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Oglas',
            fields=[
                ('ID_Oglas', models.AutoField(primary_key=True, serialize=False)),
                ('datum_objava', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('datum_odjava', models.DateTimeField(blank=True, default=datetime.datetime(2018, 11, 28, 21, 4, 49, 529100))),
                ('prioritetna_vrsta', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Stanovanje',
            fields=[
                ('ID_Stanovanje', models.AutoField(primary_key=True, serialize=False)),
                ('vrsta', models.IntegerField()),
                ('sobno', models.IntegerField()),
                ('št_študentov', models.IntegerField()),
                ('ime_stanovanje', models.CharField(max_length=35)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=6)),
                ('ulica', models.CharField(max_length=45)),
                ('hš', models.CharField(max_length=35)),
                ('kadilci', models.IntegerField()),
                ('ljubljenčki', models.IntegerField()),
                ('spol', models.IntegerField()),
                ('ID_Pošta', models.ForeignKey(on_delete=None, related_name='Pošta', to='stanovanje.Naslov')),
            ],
        ),
        migrations.CreateModel(
            name='Termin_ogledov',
            fields=[
                ('ID_Termin', models.AutoField(primary_key=True, serialize=False)),
                ('datum_ogleda', models.DateTimeField(blank=True, default=None)),
                ('začetek_ogleda', models.CharField(max_length=7)),
                ('konec_ogleda', models.CharField(max_length=7)),
                ('prosto', models.IntegerField()),
                ('max_ogledov', models.IntegerField()),
                ('ID_Oglas', models.ForeignKey(on_delete=None, related_name='Oglas', to='stanovanje.Oglas')),
            ],
        ),
        migrations.CreateModel(
            name='Uporabnik',
            fields=[
                ('ID_Uporabnik', models.AutoField(primary_key=True, serialize=False)),
                ('ime_uporabnik', models.CharField(max_length=50)),
                ('priimek', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=30)),
                ('mail', models.CharField(max_length=50)),
                ('tip', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='oglas',
            name='ID_Stanovanje',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Stanovanje', to='stanovanje.Stanovanje'),
        ),
        migrations.AddField(
            model_name='oglas',
            name='ID_Uporabnik',
            field=models.ForeignKey(on_delete=None, related_name='Uporabnik', to='stanovanje.Uporabnik'),
        ),
    ]
