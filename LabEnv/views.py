from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .enviroment import Enviroment
from .status import *
import os


class EnvView(APIView):
    def get(self, request):
        response = {
            "ENV": Enviroment.env,
        }
        return Response(response)


class TestView(APIView):
    def get(self, request):
        response = {
            "message": "OK"
        }
        return Response(response)
