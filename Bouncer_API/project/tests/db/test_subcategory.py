from django.test import TestCase
from db.models.subcategory_model import Category, SubCategory


class CategoryTestCases(TestCase):
    def setUp(self):
        self.sub_category = SubCategory.objects.create(
            category=Category.objects.create(id='3cd2b4b0c36f43488a93b3bb72029f46'), title='Hello world',
            id='3cd2b4b0c36f43488a93b3bb72029f46')

    def test_sub_categoryTitle(self):
        self.assertTrue(type(self.sub_category), str)

    def test_sub_categoryLenOFTitle(self):
        self.assertTrue(len(self.sub_category.title) <= 200)

    def test_sub_categoryTitleNotNull(self):
        self.assertTrue(self.sub_category.title != '')

    def test_categoryTitleNotASingileWord(self):
        self.assertTrue(len(self.sub_category.title.split()) > 1)

    def test_categoryUUID(self):
        uuid_field = self.sub_category.id
        trutty = uuid_field.isalnum()
        self.assertTrue(trutty)
