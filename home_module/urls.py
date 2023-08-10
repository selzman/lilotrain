from django.urls import path ,include
from . import views

urlpatterns=[
    path('',views.HomeView.as_view(),name='home_page'),
    path('',include('user_module.urls')),
    path('product/<str:slug>',include('product_module.urls'))
]