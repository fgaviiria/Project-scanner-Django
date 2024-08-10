from rest_framework import viewsets
from reader.models import Product
from reader.api.serializer import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

