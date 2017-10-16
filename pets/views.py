from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Cat, Dog
from .serializers import CatSerializer, DogSerializer


class CatViewSet(viewsets.ModelViewSet):
    serializer_class = CatSerializer

    def get_queryset(self):
        return self.request.user.cats.all()

class DogViewSet(viewsets.ModelViewSet):
    serializer_class = DogSerializer
    def get_queryset(self):
        return self.request.user.dogs.all()

def index(request):
    return HttpResponse("test view")
