from rest_framework import serializers
from shortner.models import UrlModels


class UrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UrlModels
        fields = '__all__'