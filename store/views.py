from django.shortcuts import render
from django.shortcuts import render

from django.shortcuts import render
from rest_framework import generics
from .serializer import StoreSerializer
from .models import Store
from .permissions import IsAuthorOrReadOnly


class StoreList(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class StoreDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
