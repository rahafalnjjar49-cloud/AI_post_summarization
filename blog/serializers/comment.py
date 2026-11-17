from rest_framework import serializers
from ..models import comment
class CommentSerializers (serializers.ModelSerializer):
    class Meta:
        model = comment
        fields = '__all__'
        read_only_fields = ('id',)
