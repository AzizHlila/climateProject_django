from django.shortcuts import render
from rest_framework.views import APIView
from api.serializers import FactorsSerializer,InformationSerializer
from rest_framework.response import Response
from api.generate_chart import getPayeChart

from api.models import Factors,Information
from django.http import HttpResponse, FileResponse


# Create your views here.
# Create your views here.

class FactorsView(APIView):
    def get(self,request):
        output = [{"name":out.name,
                   "description":out.description,
                    }
                   for out in Factors.objects.all()]
        return Response(output)
    
    def post(self,request):
        serializer =  FactorsSerializer(data=request.data)
        if(serializer.is_valid(raise_exception=True)):
            serializer.save()
            return Response(serializer.data)

class InformationView(APIView):
    def get(self,request):
        output = [{"title":out.title,
                   "description":out.description,
                   "is_true":out.is_true,
                    }
                   for out in Information.objects.all()]
        return Response(output)
    
    def post(self,request):
        serializer =  InformationSerializer(data=request.data)
        if(serializer.is_valid(raise_exception=True)):
            serializer.save()
            return Response(serializer.data)

def chart_view(request, country):
    # Assuming getPayeChart returns a BytesIO containing the image
    image_buffer = getPayeChart(country)

    # Create a Django response with the image content
    response = HttpResponse(image_buffer, content_type='image/png')
    
    # Optionally, set a filename for the browser to use when saving the image
    response['Content-Disposition'] = 'attachment; filename="chart.png"'

    return response