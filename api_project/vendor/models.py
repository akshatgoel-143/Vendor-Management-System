from django.db import models
from django.db.models import Avg, Count, F, ExpressionWrapper
from django.db.models.functions import Coalesce

# Create your models here.

class Vendor(models.Model):

    name = models.CharField(max_length=50)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=20, unique=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return self.name
    
    def update_performance_metrics(self):
        from purchase.models import Purchase
        total_completed_orders = Purchase.objects.filter(status='completed').count()
        if total_completed_orders > 0:
            # On-Time Delivery Rate
            on_time_delivered_orders = Purchase.objects.filter(
                status='completed', delivery_date__lte=models.F('acknowledgment_date')
            ).count()
            self.on_time_delivery_rate = on_time_delivered_orders / total_completed_orders

            # Quality Rating Average
            self.quality_rating_avg = Purchase.objects.filter(
                status='completed', quality_rating__isnull=False
            ).aggregate(avg_quality_rating=Avg('quality_rating'))['avg_quality_rating'] or 0

            # Average Response Time

            orders = Purchase.objects.filter(
                status='completed', acknowledgment_date__isnull=False
            )
            total_response_time = 0
            for order in  orders:
                response_time = (order.issue_date - order.acknowledgment_date).days
                total_response_time += response_time
            self.average_response_time = total_response_time / len(orders)


            # Fulfilment Rate
            successfully_fulfilled_orders = Purchase.objects.filter(
                status='completed', delivery_date__lte=models.F('acknowledgment_date')
            ).count()
            self.fulfilment_rate = successfully_fulfilled_orders / total_completed_orders
        else:
            # Reset metrics if there are no completed orders
            self.on_time_delivery_rate = 0
            self.quality_rating_avg = 0
            self.average_response_time = 0
            self.fulfilment_rate = 0

        self.save()

class HistoricalPerformance(models.Model):

    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return str(self.vendor_id.name)