from django.urls import path
from .views import dashboard, products, customer

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("products/", products, name="products"),
    # path("customer/", customer, name="customer-list"),
    path("customer/<int:pk>/", customer, name="customer-detail"),
]
