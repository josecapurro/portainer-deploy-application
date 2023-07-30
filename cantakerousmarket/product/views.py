from django.shortcuts import render
from rest_framework import viewsets
from product.serializers import ProductSerializer
from product.models import Product
from django.views.generic import View

# Create your views here.

class ProductView(View):
    template_name = 'product.html'
    def get(self, request):
        return render(request, self.template_name)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



