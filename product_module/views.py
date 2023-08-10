
from django.views.generic import ListView
from .models import Product ,Comment
from .forms import Newcomments
# Create your views here.

class ProductDetailView(ListView):
    template_name = 'product_module/product.html'
    model = Product
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        context['Products'] = Product.objects.filter(activate=True)
        context['newcomments'] = Newcomments
        context['Comments'] = Comment.objects.filter(is_active=True,parent=None).prefetch_related('comment_set')
        return context
