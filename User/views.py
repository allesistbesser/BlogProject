from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import serializers, status
from .serializers import RegisterSerializer
from rest_framework.generics import CreateAPIView , ListCreateAPIView
from rest_framework.response import Response

class RegisterApi(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
    def get(self, request):
        user = User.objects.all()
        serializer = RegisterSerializer(user, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

