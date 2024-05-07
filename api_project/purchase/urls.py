from django.urls import path
from .import views
urlpatterns = [
    path('', views.PurchaseAPI.as_view(), name="purchase_orders"),
    path('<int:id>', views.PurchaseAPI.as_view(), name="purchase_order"),
    path('<int:id>/acknowledge', views.PurchaseAPI.as_view(), name="acknowledge")
]
