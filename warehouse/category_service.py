from .category_repository import CategoryRepository    



class CategoryService:
    @staticmethod
    def list_all_categories():
        return CategoryRepository.get_all_categories()
    
    @staticmethod
    def add_category(category_data, request):
        return CategoryRepository.create_category(category_data, request)
    
    @staticmethod
    def get_category_by_id(pk):
        return CategoryRepository.get_category(pk)
    
    @staticmethod
    def modify_category(pk, update_data):
        return CategoryRepository.update_category(pk, update_data)
    
    @staticmethod
    def remove_category(pk):
        category = CategoryRepository.get_category(pk)
        if category:
            CategoryRepository.delete_category(category)
            return True
        return False
    
    @staticmethod
    def fetch_categoryproducts(pk):
        return CategoryRepository.find_categoryproducts(pk)

    
