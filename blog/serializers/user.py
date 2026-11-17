from rest_framework import serializers
from ..models import user

class UserSerializers (serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'
        read_only_fields = ('id',)