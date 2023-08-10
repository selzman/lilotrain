from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from product_module.models import Product
# Create your views here.


class HomeView(ListView):
    template_name = 'home_page.html'
    model = Product
    print(Product.slug)


    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['products'] = Product.objects.get()

        return context

