from django.test import TestCase
from db.models.category_model import Category


class CategoryTestCases(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(
            title='Foot wears', id='3cd2b4b0c36f43488a93b3bb72029f46')

    def test_categoryTitle(self):
        self.assertTrue(type(self.category1), str)

    def test_categoryLenOFTitle(self):
        self.assertTrue(len(self.category1.title) <= 200)

    def test_categoryTitleNotNull(self):
        self.assertTrue(self.category1.title != '')

    def test_categoryTitleNotNull(self):
        self.assertTrue(len(self.category1.title.split()) > 1)

    def test_categoryDateCheck(self):
        created_date = self.category1.created_at
        updated_date = self.category1.updated_at
        self.assertTrue(created_date < updated_date)

    def test_categoryUUID(self):
        uuid_field = self.category1.id
        trutty = uuid_field.isalnum()
        self.assertTrue(trutty)

    def test_categoryDateCreatedVerboseName(self):
        created_label = self.category1.created_at
        date = Category.objects.get(created_at=created_label)
        field_label = date._meta.get_field('created_at').verbose_name
        self.assertEqual(field_label, 'created at')

    def test_categoryDateUpdatedVerboseName(self):
        updated_label = self.category1.updated_at
        date = Category.objects.get(updated_at=updated_label)
        field_label = date._meta.get_field('updated_at').verbose_name
        self.assertEqual(field_label, 'updated at')
