from django.urls import path
from .import views
urlpatterns = [
    path('', views.VendorAPI.as_view(), name="vendors"),
    path('<int:id>', views.VendorAPI.as_view(), name="vendor"),
    path('<int:id>/performance', views.VendorPerformance.as_view(), name="performance")
]