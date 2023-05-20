from django.shortcuts import render
from .models import Product, Order, Customer


# Create your views here.
def dashboard(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    pending = orders.filter(status="Pending").count()
    delivered = orders.filter(status="Delivered").count()

    context = {
        "orders": orders,
        "customers": customers,
        "total_orders": total_orders,
        "pending": pending,
        "delivered": delivered,
    }
    return render(request, "accounts/dashboard.html", context)


def products(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "accounts/products.html", context)


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    orders_count = orders.count()
    context = {"customer": customer, "orders": orders, "orders_count": orders_count}
    return render(request, "accounts/customer.html", context)
