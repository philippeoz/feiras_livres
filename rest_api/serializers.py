from rest_framework import serializers
from core.models import FeiraLivre


class FeiraLivreSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeiraLivre
        fields = '__all__'
