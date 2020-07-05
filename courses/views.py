from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import CourseModel
from .serializers import CourseSerializer


class CourseView(viewsets.ModelViewSet):
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer
