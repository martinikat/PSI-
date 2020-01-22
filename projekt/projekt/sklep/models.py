from django.db import models

class Klient(models.Model):
    idKlienta=models.IntegerField(primary_key=True)
    imie=models.CharField(max_length=30)
    nazwisko=models.CharField(max_length=30)
    numerTelefonu=models.IntegerField()

class Produkt(models.Model):
    idProduktu=models.IntegerField(primary_key=True)
    rodzaj=models.CharField(max_length=30)
    ilosc=models.IntegerField()

class Zamowienie(models.Model):
    idZamowienia=models.IntegerField(primary_key=True)
    idKlienta=models.ForeignKey(Klient, on_delete=models.CASCADE)
    idProduktu=models.ForeignKey(Produkt, on_delete=models.CASCADE)
    ilosc=models.IntegerField()
    owner = models.ForeignKey('auth.User', related_name='Zamowienia', on_delete=models.CASCADE);