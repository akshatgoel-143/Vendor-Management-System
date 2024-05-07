from django.db import models
import vendor
from vendor.models import Vendor
# Create your models here.

class Purchase(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('pending', 'Pending'),
        ('cancelled', 'Cancelled'),
    ]

    po_number = models.CharField(max_length=20, unique=True)
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    quality_rating = models.FloatField()
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField()

    def __str__(self):
        return self.po_number
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.status == 'completed':
            self.vendor_id.update_performance_metrics()
