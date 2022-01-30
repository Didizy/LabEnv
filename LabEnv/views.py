from rest_framework.views import APIView
from rest_framework.response import Response
from .status import *


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
