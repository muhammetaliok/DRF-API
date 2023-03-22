from rest_framework.serializers import ModelSerializer
from .models import Note
from rest_framework import serializers

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

