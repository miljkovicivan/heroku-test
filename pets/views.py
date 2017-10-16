from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .models import Cat, Dog
from .serializers import CatSerializer, DogSerializer


class CatViewSet(viewsets.ModelViewSet):
    serializer_class = CatSerializer
    permission_classesa = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.cats.all()

class DogViewSet(viewsets.ModelViewSet):
    serializer_class = DogSerializer
    permission_classesa = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.dogs.all()

def index(request):
    return HttpResponse("test view")
