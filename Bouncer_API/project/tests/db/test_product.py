from django.test import TestCase
from db.models.product import *


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        brand_phone = Brand.objects.create(name="Applw")
        # rating_phone= Rating.objects.create(name="5star")
        category_phone = Category.objects.create(title="Phones")
        # label_phone = Label.objects.create(name="A digital tool of the century")
        Product.objects.create(
            name='iphone 13',
            price='700.50',
            category=category_phone,
            discounted_price=6900,
            shipping_fee=5000,
            quantity_in_stock=20000,
            ratings=2.5,
            brand=brand_phone,
        )

    def test_discounted_price_label(self):
        new_id = Product.objects.all().first().id
        product = Product.objects.get(id=new_id)
        product_label = product._meta.get_field(
            'discounted_price').verbose_name
        self.assertEqual(product_label, 'discounted price')

    def test_quantity_in_stock_label(self):
        new_id = Product.objects.all().first().id
        product = Product.objects.get(id=new_id)
        product_label = product._meta.get_field(
            'quantity_in_stock').verbose_name
        self.assertEqual(product_label, 'quantity in stock')

    def test_name_max_length(self):
        new_id = Product.objects.all().first().id
        product = Product.objects.get(id=new_id)
        max_length = product._meta.get_field('name').max_length
        self.assertEqual(max_length, 30)

    def test_created_at_label(self):
        new_id = Product.objects.all().first().id
        product = Product.objects.get(id=new_id)
        product_label = product._meta.get_field('created_at').verbose_name
        self.assertEqual(product_label, 'created at')

    def test_updated_at_label(self):
        new_id = Product.objects.all().first().id
        product = Product.objects.get(id=new_id)
        product_label = product._meta.get_field('updated_at').verbose_name
        self.assertEqual(product_label, 'updated at')

    def test_product_model(self):
        new_id = Product.objects.all().first().id
        product = Product.objects.get(id=new_id)
        self.assertEqual(str(product), 'iphone 13')
