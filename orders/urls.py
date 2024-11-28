from django.urls import path
from . import views

urlpatterns = [
    path('summary/', views.order_summary, name='order_summary'),
]
