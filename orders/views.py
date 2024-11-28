from django.shortcuts import render

def order_summary(request):
    return render(request, 'orders/order_summary.html')

