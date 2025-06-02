from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from mongoengine.errors import ValidationError as MongoValidationError

class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            try:
                product = serializer.save()
                response_data = {
                    "id": str(product.id),
                    "name": product.name,
                    "description": product.description,
                    "price": product.price,
                    "stock": product.stock
                }
                return Response(response_data, status=status.HTTP_201_CREATED)
            except MongoValidationError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        product = Product.objects(id=pk).first()
        if not product:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(ProductSerializer(product).data)

    def update(self, request, pk=None):
        product = Product.objects(id=pk).first()
        if not product:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            return Response(ProductSerializer(product).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        product = Product.objects(id=pk).first()
        if not product:
            return Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        product.delete()
        return Response({'message': 'Producto eliminado correctamente'}, status=status.HTTP_200_OK)

