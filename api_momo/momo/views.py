from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from python.MoMo import MomoResponse

class ResponseMomo(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        # amount = request.query_params['amount']
        
        amount = request.GET.get('amount')
        print(amount)
        data = MomoResponse(amount)
        print(data)
        return Response(data)

responseMomo = ResponseMomo.as_view()