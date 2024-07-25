from .models import Subject
from rest_framework import serializers

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['subject_name', 'professor', 'students']



