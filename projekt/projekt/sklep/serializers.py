from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = ['idKlient','imie','nazwisko','numerTelefonu']

class ProduktSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produkt
        fields = ['idProduktu','rodzaj','ilosc']

class ZamowienieSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Zamowienie
        fields = ['idZamowienia','idKlienta','idProduktu','ilosc']

class UserSerializer(serializers.ModelSerializer):
    Zamowienia = serializers.PrimaryKeyRelatedField(many=True, queryset=Zamowienie.objects.all())
    class Meta:
        model = User
        fields = ['id','username', 'Zamowienia']