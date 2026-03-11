from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Students
from .serializers import *

# Create your views here.

@api_view(["GET"])
def home(request):
    student_objs = Students.objects.all()
    serializer = StudentsSerializer(student_objs,many= True)
    return Response({'status':200, 'message':'Hello From Django Rest Framework','payload' : serializer.data})