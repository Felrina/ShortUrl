# from rest_framework import viewsets
# from shortner.models import UrlModels
# from rest_framework import permissions
# from shortner.serializers import UrlSerializer

# class UrlViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = UrlModels.objects.all()
#     serializer_class = UrlSerializer
#     permission_classes = [permissions.IsAuthenticated]

from django.shortcuts import render
from rest_framework import generics
from shortner.models import UrlModels
from shortner.serializers import UrlSerializer


class URL_objects(generics.ListCreateAPIView):
    queryset = UrlModels.objects.all()
    serializer_class = UrlSerializer
class URL_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = UrlModels.objects.all()
    serializer_class = UrlSerializer