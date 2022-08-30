from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST','GET'])
def home(request):
    return Response({"message": "Hello, world!", 'status': 200})
