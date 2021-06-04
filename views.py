from django.shortcuts import render
from .models import Oxygen_Leads
from django.http import JsonResponse
from .serializers import Oxy_Serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from rest_framework import status
# Create your views here.
@api_view(['GET','POST'] )
def oxy_lead(request):
    if request.method == "GET":
        lead_data = Oxygen_Leads.objects.all()
        serializer = Oxy_Serializer(lead_data, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Oxy_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

