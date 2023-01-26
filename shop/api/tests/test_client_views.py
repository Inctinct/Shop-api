from django.test import TestCase
from ..models import Category
from django.urls import reverse


class TestCategoriesView(TestCase):
    fixtures = ["api/tests/fixtures/fixture_categories.json"]

    def test_categories_all_view(self):
        response = self.client.get(reverse('categories-all'))
        self.assertIsInstance(response.data, list)
        self.assertEqual(response.data, [
            {
                "id": 1,
                "name": "category1",
                "description": "some description"
            }
        ])


class TestDiscountsView(TestCase):
    fixtures = ["api/tests/fixtures/fixture_discounts.json"]

    def test_discount_all_view(self):
        response = self.client.get(reverse('discounts-all'))
        self.assertIsInstance(response.data, list)
        self.assertEqual(response.data, [
            {
                "id": 1,
                "name": "discount1",
                "percent": 10,
                "expire_date": "2022-12-27T16:32:32Z"
            }

        ])


class TestProducersView(TestCase):
    fixtures = ["api/tests/fixtures/fixture_producers.json"]

    def test_producer_all_view(self):
        response = self.client.get(reverse('producers-all'))
        self.assertIsInstance(response.data, list)
        self.assertEqual(response.data, [
            {
                "id": 1,
                "name": "producer1"
            }
        ])


class TestPromocodesView(TestCase):
    fixtures = ["api/tests/fixtures/fixture_promocodes.json"]

    def test_promocode_all_view(self):
        response = self.client.get(reverse('promocodes-all'))
        self.assertIsInstance(response.data, list)
        self.assertEqual(response.data, [
            {
                "id": 1,
                "name": "promocode",
                "percent": 10,
                "expire_date": "2022-12-27T16:32:32Z",
                "is_allowed_to_sum_with_discount": True
            }
        ])


class TestProductsView(TestCase):
    fixtures = ["api/tests/fixtures/fixture_producers.json",
                "api/tests/fixtures/fixture_categories.json",
                "api/tests/fixtures/fixture_discounts.json",
                "api/tests/fixtures/fixture_products.json"
                ]

    def test_product_all_view(self):
        response = self.client.get(reverse('products-all'))
        self.assertIsInstance(response.data, list)
        # print(response.data)
        self.assertEqual(response.data, [
            {
                'id': 1,
                "name": "product123",
                "description": "test123",
                "producer": {
                    "id": 1,
                    "name": "producer1"
                },
                "category": {
                    "id": 1,
                    "name": "category1",
                    "description": "some description"
                },
                "discount": {
                    "id": 1,
                    "name": "discount1",
                    "percent": 10,
                    "expire_date": "2022-12-27T16:32:32Z"
                },
                "price": 5.99,
                "articul": "123",
                "count_on_stock": 100,

            }
        ])