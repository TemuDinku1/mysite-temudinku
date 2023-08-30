from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Category, Product
from .serializers import ProductSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/product',
        'GET /api/product/:id',
    ]
    return Response(routes)


@api_view(['GET'])
def getProduct(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)
