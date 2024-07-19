from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer
from rest_framework.response import Response
# Create your views here.
@api_view(['POST'])
def registration(request):
    if request.method=='POST':
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Success"})
        else:
            return Response({"msg":"Failed"})