from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Vendor, HistoricalPerformance
from .serializers import VendorSerializer, HistoricalPerformanceSerializer
from datetime import datetime
# Create your views here.


class VendorAPI(APIView):

    def get(self, request, id=None, format=None):
        if id:
            vendor = Vendor.objects.get(pk=id)
            serializer = VendorSerializer(vendor)
            return Response(serializer.data)
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'vendor created'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Error'}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, id=None, format=None):
        if id:
            vendor = Vendor.objects.get(pk=id)
            serializer = VendorSerializer(vendor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Vendor Updated'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'Error'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Id not found'}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, id=None, format=None):
        if id:
            vendor = Vendor.objects.get(pk=id)
            serializer = VendorSerializer(vendor, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Vendor Updated'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'Error'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Id not found'}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None, format=None):
        if id:
            vendor = Vendor.objects.get(pk=id)
            vendor.delete()
            return Response({'message': 'Vendor Deleted'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Id not found'}, status=status.HTTP_400_BAD_REQUEST)
        

class VendorPerformance(APIView):

    def get(self, request, id=None, format=None):
        if id:
            vendor = Vendor.objects.get(pk=id)
            performance = HistoricalPerformance.objects.create(
                vendor_id=vendor,
                date=datetime.now(),
                on_time_delivery_rate=vendor.on_time_delivery_rate,
                quality_rating_avg=vendor.quality_rating_avg,
                average_response_time=vendor.average_response_time,
                fulfillment_rate=vendor.fulfillment_rate,
            )
            serializer = HistoricalPerformanceSerializer(performance)
            return Response(serializer.data)
        else:
            return Response({'message': 'Id not found'}, status=status.HTTP_400_BAD_REQUEST)