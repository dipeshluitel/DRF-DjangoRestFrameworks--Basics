from rest_framework import serializers
from .models import *
class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['name', 'age']

    def validate(self,data):
        if data['age'] <= 18 :
            raise serializers.ValidationError({'age':'Age cannot be less than 18 years'})
        return data
