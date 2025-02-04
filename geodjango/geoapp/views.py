from django.shortcuts import render
from rest_framework import viewsets
from .models import Place
from .serializers import PlaceSerializer
# Create your views here.


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
