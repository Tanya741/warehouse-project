import unittest
from unittest.mock import patch, MagicMock
from warehouse.category_service import CategoryService


class CategoryServiceTest(unittest.TestCase):

    @patch('warehouse.category_service.CategoryRepository')
    def test_add_category(self, MockCategoryRepository):
        mock_category = MagicMock()
        mock_category.pk =1
        MockCategoryRepository.create_category.return_value = mock_category

        category_data  = {
            'title': 'Category 1',
            'description': 'Category Description',
            'published_date': None
        }

        category = CategoryService.add_category(category_data, None)

        MockCategoryRepository.create_category.assert_called_once_with(category_data, None)
        self.assertEqual(category.pk, 1)

    @patch('warehouse.category_service.CategoryRepository')
    def test_get_category_by_id(self, MockCategoryRepository):
        # Mock the CategoryRepository's get_category method
        mock_category = MagicMock()
        mock_category.pk = 1
        MockCategoryRepository.get_category.return_value = mock_category

        # Call the service method
        category = CategoryService.get_category_by_id(1)

        # Assertions
        MockCategoryRepository.get_category.assert_called_once_with(1)
        self.assertEqual(category.pk, 1)

    @patch('warehouse.category_service.CategoryRepository')
    def test_list_all_categories(self, MockCategoryRepository):
        # Mock the CategoryRepository's get_all_categories method
        mock_categories = [MagicMock(), MagicMock()]
        MockCategoryRepository.get_all_categories.return_value = mock_categories

        # Call the service method
        categories = CategoryService.list_all_categories()

        # Assertions
        MockCategoryRepository.get_all_categories.assert_called_once()
        self.assertEqual(len(categories), 2)

    @patch('warehouse.category_service.CategoryRepository')
    def test_modify_category(self, MockCategoryRepository):
        # Mock the CategoryRepository's update_category method
        mock_category = MagicMock()
        mock_category.pk = 1
        MockCategoryRepository.update_category.return_value = mock_category

        update_data = {'title': 'Updated Category'}

        # Call the service method
        category = CategoryService.modify_category(1, update_data)

        # Assertions
        MockCategoryRepository.update_category.assert_called_once_with(1, update_data)
        self.assertEqual(category.pk, 1)

    @patch('warehouse.category_service.CategoryRepository')
    def test_remove_category(self, MockCategoryRepository):
        mock_category = MagicMock()
        mock_category.pk =1
        MockCategoryRepository.get_category.return_value = mock_category
        MockCategoryRepository.delete_category.return_value = None

        result = CategoryService.remove_category(1)

        MockCategoryRepository.get_category.assert_called_once_with(1)
        MockCategoryRepository.delete_category.assert_called_once_with(mock_category)
        self.assertTrue(result)

        MockCategoryRepository.reset_mock()
        MockCategoryRepository.get_category.return_value = None

        result = CategoryService.remove_category(2)

        MockCategoryRepository.get_category.assert_called_once_with(2)
        MockCategoryRepository.delete_category.assert_not_called()
        self.assertFalse(result)

    @patch('warehouse.category_service.CategoryRepository')
    def test_fetch_categoryproducts(self, MockCategoryRepository):
        mock_products = [MagicMock(), MagicMock()]
        MockCategoryRepository.find_categoryproducts.return_value = mock_products

        products = CategoryService.fetch_categoryproducts(1)

        MockCategoryRepository.find_categoryproducts.assert_called_once_with(1)
        self.assertEqual(len(products), 2)
()


