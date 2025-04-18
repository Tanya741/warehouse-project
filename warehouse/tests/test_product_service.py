import unittest
from unittest.mock import patch, MagicMock
# from django.test import TestCase
from warehouse.product_service import ProductService

class ProductServiceTest(unittest.TestCase):

    @patch('warehouse.product_service.ProductRepository')
    def test_add_product(self, MockProductRepository):
        mock_product = MagicMock()
        mock_product.pk = 1
        MockProductRepository.create_product.return_value= mock_product

        product_data = {
            'name': 'Product 1',
            'description': 'Product description',
            'category': 'category 1',
            'price': 20.5,
            'brand': 'Brand A',
            'quantity': 10,
            'published_date': None
        }
        product = ProductService.add_product(product_data, None)
        MockProductRepository.create_product.assert_called_once_with(product_data, None)
        self.assertEqual(product.pk, 1)

    @patch('warehouse.product_service.ProductRepository')
    def test_get_product_by_id(self, MockProductRepository):
        mock_product = MagicMock()
        mock_product.pk = 1
        MockProductRepository.get_product.return_value = mock_product

        product =  ProductService.get_product_by_id(1)

        MockProductRepository.get_product.assert_called_once_with(1)
        self.assertEqual(product.pk, 1)

    @patch('warehouse.product_service.ProductRepository')
    def test_modify_product(self, MockProductRepository):
        mock_product = MagicMock
        mock_product.pk = 1
        MockProductRepository.update_product.return_value = mock_product

        update_data = {'name': 'Updated Product'}

        product = ProductService.modify_product(1, update_data)

        MockProductRepository.update_product.assert_called_once_with(1, update_data)
        self.assertEqual(product.pk, 1)

    @patch('warehouse.product_service.ProductRepository')
    def test_list_all_products(self, MockProductRepository):
        mock_products = [MagicMock(), MagicMock()]
        MockProductRepository.get_all_products.return_value = mock_products

        products = ProductService.list_all_products()

        MockProductRepository.get_all_products.assert_called_once()
        self.assertEqual(len(products), 2)


    @patch('warehouse.product_service.ProductRepository')
    def test_remove_product(self, MockProductRepository):
        mock_product = MagicMock()
        mock_product.pk =1
        MockProductRepository.get_product.return_value = mock_product
        MockProductRepository.delete_product.return_value = None

        result = ProductService.remove_product(1)

        MockProductRepository.get_product.assert_called_once_with(1)
        MockProductRepository.delete_product.assert_called_once_with(mock_product)
        self.assertTrue(result)

        #To check when Product does not exist
        MockProductRepository.reset_mock()
        MockProductRepository.get_product.return_value = None

        result = ProductService.remove_product(2)

        MockProductRepository.get_product.assert_called_once_with(2)
        MockProductRepository.delete_product.assert_not_called()
        self.assertFalse(result)

    @patch('warehouse.product_service.ProductRepository')
    def test_fetch_product(self, MockProductRepository):
        mock_products =[MagicMock(), MagicMock()]
        MockProductRepository.find_product.return_value = mock_products

        products = ProductService.fetch_product("Product")

        MockProductRepository.find_product.assert_called_once_with("Product")
        self.assertEqual(len(products), 2)

    




