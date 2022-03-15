from django.test import TestCase
from clean_city.models.user_model import User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(first_name='John', last_name='Doe', email='johndoe@gmail.com', phone='+234-7065'
                                                                                                          '-1234',
                            password='johndoe')

    def test_first_name_label(self):
        user = User.objects.all().first()
        field_label = user._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_last_name_label(self):
        user = User.objects.all().first()
        field_label = user._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'last name')

    def test_phone_number_label(self):
        user = User.objects.all().first()
        field_label = user._meta.get_field('phone').verbose_name
        self.assertEqual(field_label, 'phone')

    def test_created_at_label(self):
        user = User.objects.all().first()
        field_label = user._meta.get_field('created_at').verbose_name
        self.assertEqual(field_label, 'created at')

    def test_updated_at_label(self):
        user = User.objects.all().first()
        field_label = user._meta.get_field('updated_at').verbose_name
        self.assertEqual(field_label, 'updated at')

    def test_max_length_first_name(self):
        user = User.objects.all().first()
        max_length = user._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 150)

    def test_max_length_last_name(self):
        user = User.objects.all().first()
        max_length = user._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 150)

    def test_max_length_email(self):
        user = User.objects.all().first()
        max_length = user._meta.get_field('email').max_length
        self.assertEqual(max_length, 254)

    def test_max_length_phone_number(self):
        user = User.objects.all().first()
        max_length = user._meta.get_field('phone').max_length
        self.assertEqual(max_length, 50)

    def test_max_length_password(self):
        user = User.objects.all().first()
        max_length = user._meta.get_field('password').max_length
        self.assertTrue(max_length>4)
        