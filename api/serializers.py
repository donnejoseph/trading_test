from rest_framework import serializers
from api.models import Signal


class SignalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signal
        fields = ('type', 'params',)
