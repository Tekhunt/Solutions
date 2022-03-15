from django.test import TestCase

from db.models.user_model import User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(first_name='John', last_name='Bull', email='johnbull@gmail.com', phone_number='+234-7065'
                                                                                                          '-1234',
                            password='johnbull', otp_code='12345')

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
        field_label = user._meta.get_field('phone_number').verbose_name
        self.assertEqual(field_label, 'phone number')

    def test_otp_code_label(self):
        user = User.objects.all().first()
        field_label = user._meta.get_field('otp_code').verbose_name
        self.assertEqual(field_label, 'otp code')

    def test_email_verified(self):
        user = User.objects.all().first()
        field_label = user._meta.get_field('email_verified').verbose_name
        self.assertEqual(field_label, 'email verified')

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
        self.assertEqual(max_length, 30)

    def test_max_length_last_name(self):
        user = User.objects.all().first()
        max_length = user._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 30)

    def test_max_length_email(self):
        user = User.objects.all().first()
        max_length = user._meta.get_field('email').max_length
        self.assertEqual(max_length, 50)

    def test_max_length_phone_number(self):
        user = User.objects.all().first()
        max_length = user._meta.get_field('phone_number').max_length
        self.assertEqual(max_length, 50)

    def test_max_length_password(self):
        user = User.objects.all().first()
        max_length = user._meta.get_field('password').max_length

        self.assertEqual(max_length, 15)
        


    def test_max_length_otp_code(self):
        user = User.objects.all().first()
        max_length = user._meta.get_field('otp_code').max_length
        self.assertEqual(max_length, 6)
