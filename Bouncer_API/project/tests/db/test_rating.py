from django.test import TestCase
from db.models.rating_models import *
from db.models.category_model import Category
from db.models.brand import Brand


class RatingsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        brand_phone = Brand.objects.create(name="Applw")
        category_phone = Category.objects.create(title="Phones")
        product = Product.objects.create(
            name='handbag',
            price='700.50',
            category=category_phone,
            discounted_price=6900,
            shipping_fee=5000,
            quantity_in_stock=20000,
            ratings=2.5,
            brand=brand_phone,
        )
        Rating.objects.create(score=3.5, product=product, review='Good')

    def test_score_label(self):
        rating = Rating.objects.all().first()
        decimal_places = rating._meta.get_field('score').decimal_places
        self.assertEqual(decimal_places, 1)

    def test_str_method(self):
        rating = Rating.objects.all().first()
        self.assertEqual(str(rating), 'rating for handbag')

    def test_score_max_digit(self):
        rating = Rating.objects.all().first()
        max_digit = rating._meta.get_field('score').max_digits
        self.assertEqual(max_digit, 2)

    def test_review_max_length(self):
        rating = Rating.objects.all().first()
        max_length = rating._meta.get_field('review').max_length
        self.assertEqual(max_length, 200)

    def test_rating_id_label(self):
        rating = Rating.objects.all().first()
        field_label = rating._meta.get_field('rating_id').verbose_name
        self.assertEqual(field_label, 'rating id')
