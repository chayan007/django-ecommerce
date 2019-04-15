from django.shortcuts import render
from django.views.generic import ListView
from .models import Products

# Create your views here.


class ProductListView(ListView):
    queryset = Products.objects.all()
    template_name = 'products/product_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        return context


