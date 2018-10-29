from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
from datetime import timedelta


class Naslov(models.Model):
    ID_Pošta = models.AutoField(primary_key=True)
    ime_pošta = models.CharField(max_length=35)

class Stanovanje(models.Model):
    ID_Stanovanje = models.AutoField(primary_key=True)
    ID_Pošta = models.ForeignKey(Naslov, on_delete=None,related_name='Pošta')
    vrsta = models.IntegerField()
    sobno = models.IntegerField()
    št_študentov = models.IntegerField()
    ime_stanovanje = models.CharField(max_length=35)
    cena = models.DecimalField(max_digits=6, decimal_places=2)
    ulica =  models.CharField(max_length=45)
    hš = models.CharField(max_length=35)
    kadilci = models.IntegerField()
    ljubljenčki = models.IntegerField()
    spol = models.IntegerField()

class Uporabnik(models.Model):
    ID_Uporabnik = models.AutoField(primary_key=True)
    ime_uporabnik = models.CharField(max_length=50)
    priimek = models.CharField(max_length=50)
    tel = models.CharField(max_length=30)
    mail = models.CharField(max_length=50)
    tip = models.IntegerField()

class Oglas(models.Model):
    ID_Oglas = models.AutoField(primary_key=True)
    ID_Uporabnik = models.ForeignKey(Uporabnik, on_delete=None, related_name='Uporabnik')
    ID_Stanovanje = models.ForeignKey(Stanovanje, on_delete=models.CASCADE, related_name='Stanovanje')
    datum_objava = models.DateTimeField(default=datetime.now, blank=True)
    datum_odjava =  models.DateTimeField(default= datetime.now() + timedelta(days=30), blank=True)
    prioritetna_vrsta = models.DecimalField(max_digits=6, decimal_places=2)


class Termin_ogledov(models.Model):
    ID_Termin = models.AutoField(primary_key=True)
    ID_Oglas = models.ForeignKey(Oglas, on_delete=None, related_name='Oglas')
    datum_ogleda = models.DateTimeField(default=None, blank=True)
    začetek_ogleda = models.CharField(max_length=7)
    konec_ogleda = models.CharField(max_length=7)
    prosto = models.IntegerField()
    max_ogledov = models.IntegerField()

