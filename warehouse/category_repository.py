from .models import Category
from django.utils import timezone
class CategoryRepository:
    @staticmethod
    def get_all_categories():
         return Category.objects.all().order_by('title')
    
    @staticmethod
    def create_category(category_data, request):
         category = Category(**category_data)
         category.author = request.user
         category.save()
         return category
    
    @staticmethod
    def get_category(pk):
         return Category.objects.get(pk=pk)
    
    @staticmethod
    def update_category(pk, update_data):
          category=Category.objects(pk=pk).first()
          if category:
              category.update(**update_data)
              category.update(published_date = timezone.now())
              category.reload()
          return category
    
    @staticmethod
    def delete_category(category):
         category.delete()
         return
    @staticmethod
    def find_categoryproducts(pk):
         category = Category.objects.get(pk=pk)
         return category.get_products()


     
         
    
          