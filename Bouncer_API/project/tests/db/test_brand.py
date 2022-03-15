from django.test import TestCase
from db.models import Brand


class BrandModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Brand.objects.create(name='iphones')

    def test_brand_max_length(self):
        new_id = Brand.objects.all().first().id
        brand = Brand.objects.get(id=new_id)
        max_length = brand._meta.get_field('name').max_length
        self.assertEqual(max_length, 30)

    def test_brand_label(self):
        new_id = Brand.objects.all().first().id
        brand = Brand.objects.get(id=new_id)
        brand_label = brand._meta.get_field('name').verbose_name
        self.assertEqual(brand_label, 'name')

    def test_brand_name_object_field(self):
        new_id = Brand.objects.all().first().id
        brand = Brand.objects.get(id=new_id)
        self.assertEqual(str(brand), 'iphones')

    def test_brand_name(self):
        brand = Brand(name="iphones")
        self.assertEqual(brand.name, "iphones")
