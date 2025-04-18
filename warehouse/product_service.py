from .product_repository import ProductRepository

class ProductService:
    @staticmethod
    def add_product(product_data, request):
        """Business logic before saving product"""
        return ProductRepository.create_product(product_data, request)

    @staticmethod
    def get_product_by_id(pk):
        """Retrieve a single product"""
        return ProductRepository.get_product(pk)

    @staticmethod
    def list_all_products():
        """List all products"""
        return ProductRepository.get_all_products()

    @staticmethod
    def modify_product(pk, update_data):
        """Modify an existing product"""
        return ProductRepository.update_product(pk, update_data)

    @staticmethod
    # def remove_product(pk):
    #     """Delete a product"""
    #     from .repositories.product_repository import ProductRepository
    @staticmethod
    def remove_product(pk):
        """Try to delete a product by ID. Return True if deleted, False if not found."""
        product = ProductRepository.get_product(pk)
        if product:
            ProductRepository.delete_product(product)
            return True
        return False
    
    @staticmethod
    def fetch_product(name):
        return ProductRepository.find_product(name)
    
    


