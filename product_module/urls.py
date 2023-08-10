from django.urls import path ,include
from . import views

urlpatterns=[
    path('',views.ProductDetailView.as_view(),name='product-detail'),


]