from rest_framework import serializers
from .models import *
import string

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['name', 'age']

    def validate(self,data):
        if data['age'] <= 18 :
            raise serializers.ValidationError({'age':'Age cannot be less than 18 years'})
        
        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({'name':'''name shouldn't contain any digit''' })

        return data
