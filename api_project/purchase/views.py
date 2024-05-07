from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Purchase
from .serializers import PurchaseSerializer
# Create your views here.


class PurchaseAPI(APIView):

    def get(self, request, id=None, format=None):
        if id:
            purchase_order = Purchase.objects.get(pk=id)
            serializer = PurchaseSerializer(purchase_order)
            return Response(serializer.data)
        purchase_orders = Purchase.objects.all()
        serializer = PurchaseSerializer(purchase_orders, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PurchaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Purchase Order created'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Error'}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, id=None, format=None):
        if id:
            purchase = Purchase.objects.get(pk=id)
            serializer = PurchaseSerializer(purchase, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Purchase Order Updated'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'Error'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Id not found'}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, id=None, format=None):
        if id:
            purchase = Purchase.objects.get(pk=id)
            if request.data.get('acknowledgment_date'):
                serializer = PurchaseSerializer(purchase, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    purchase.vendor_id.update_performance_metrics()
                    return Response({'message': 'Purchase Order Updated'}, status=status.HTTP_201_CREATED)
                else:
                    return Response({'message': 'Error'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'acknowledgment_date not found'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Id not found'}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None, format=None):
        if id:
            purchase = Purchase.objects.get(pk=id)
            purchase.delete()
            return Response({'message': 'Purchase Order Deleted'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Id not found'}, status=status.HTTP_400_BAD_REQUEST)
