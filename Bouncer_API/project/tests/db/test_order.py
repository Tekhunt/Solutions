from django.test import TestCase
from db.models.order_model import Order, Cart
from db.models.user_model import User


class OrderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create(first_name='John', last_name='Bull', email='johnbull@gmail.com',
                                   phone_number='+234-7065-1234', password='johnbull', otp_code='12345')
        cart = Cart.objects.create(
            products="['1',2,3]", user_id=user, total_cost=23.5)

        Order.objects.create(
            cart_id=cart,
            delivery_address='17 Adeleke Adegboyega street Bariga Lagos,Nigeria',
            delivery_status='RT'
        )

    def test_delivery_address_label(self):
        order = Order.objects.all().first()
        field_label = order._meta.get_field('delivery_address').verbose_name
        self.assertEqual(field_label, 'delivery address')

    def test_delivery_status_label(self):
        order = Order.objects.all().first()
        field_label = order._meta.get_field('delivery_status').verbose_name
        self.assertEqual(field_label, 'delivery status')

    def test_delivery_address_max_length(self):
        order = Order.objects.all().first()
        field_label = order._meta.get_field('delivery_address').max_length
        self.assertEqual(field_label, 255)

    def test_delivery_status_max_length(self):
        order = Order.objects.all().first()
        field_label = order._meta.get_field('delivery_status').max_length
        self.assertEqual(field_label, 2)

    def test_order__str__return_value(self):
        order = Order.objects.all().first()
        wrapper = order.__str__()
        self.assertEqual(wrapper, 'RT')
