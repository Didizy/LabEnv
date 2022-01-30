from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .enviroment import Enviroment
from .status import *
import os


class EnvView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        response = {
            "ENV": Enviroment.env,
        }
        return Response(response, status=status.HTTP_200_OK)
