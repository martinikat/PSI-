from django.shortcuts import render

# Create your views here.

from rest_framework import status, generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.contrib.auth.models import User
from .serializers import UserSerializer

#Widok klienci
@api_view(['GET', 'POST'])
def klienci_list(request, format=None):
    if request.method == 'GET':
        klienci = Klient.objects.all()
        serializer = KlientSerializer(klienci, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = KlientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def klient_detail(request, pk, format=None):
    try:
        klient = Klient.objects.get(pk=pk)
    except Klient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = KlientSerializer(klient)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = KlientSerializer(klient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        klient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Widok produkt
@api_view(['GET', 'POST'])
def produkty_list(request, format=None):
    if request.method == 'GET':
        produkty = Produkt.objects.all()
        serializer = ProduktSerializer(produkty, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProduktSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def produkty_detail(request, pk, format=None):
    try:
        produkty = Produkt.objects.get(pk=pk)
    except Produkt.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProduktSerializer(produkty)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProduktSerializer(produkty, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        produkty.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Widok zamowienia
@api_view(['GET', 'POST'])
def zamowienia_list(request, format=None):
    if request.method == 'GET':
        zamowienia = Zamowienie.objects.all()
        serializer = ZamowienieSerializer(zamowienia, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ZamowienieSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(owner = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

@api_view(['GET', 'PUT', 'DELETE'])
def zamowienia_detail(request, pk, format=None):
    try:
        zamowienie = Zamowienie.objects.get(pk=pk)
    except Zamowienie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ZamowienieSerializer(zamowienie)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ZamowienieSerializer(zamowienie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        zamowienie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer