from .models import Product, Category
from django.utils import timezone

class ProductRepository:
    @staticmethod
    def create_product(product_data, request):
        product = Product(**product_data)
        product.author = request.user
        product.save()
        return product
    
    @staticmethod
    def get_product(pk):
        return Product.objects.get(pk=pk)
    
    @staticmethod
    def get_all_products():
        return Product.objects.all().order_by('published_date')
    
    @staticmethod
    def update_product(product_id, update_data):
        product = Product.objects(id=product_id).first()
        if product:
            product.update(**update_data)
            product.published_date = timezone.now()
            product.reload()
        return product
    
    @staticmethod
    def delete_product(product):
            product.delete()

    @staticmethod
    def find_product(name):
         return Product.objects.filter(name__icontains=name).order_by('name')
    
    
        