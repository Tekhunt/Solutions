from django.test import TestCase
from db.models.payment_model import Payment
from db.models.order_model import Order
from db.models.user_model import User
from db.models.cartmodel import Cart


class PaymentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(
            first_name='femi',
            last_name='ayesoro',
            email='femiayesoro@gmail.com',
            password='hello1234',
            otp_code='765432',
        )
        cart = Cart.objects.create(
            user_id=user,
            products={'Samsung': 'TV', 'iWatch': 'series 7', 'Apple': 'Ipad'},
            total_cost=30000.90,
        )
        order = Order.objects.create(
            cart_id=cart,
            delivery_address='7 Asajon Way, Sangotedo',
            delivery_status='ND'
        )

        Payment.objects.create(payment_status='already paid', order=order)

    def test_payment_max_length(self):
        payment_uuid = Payment.objects.all().first().id
        payment = Payment.objects.get(id=payment_uuid)
        max_length = payment._meta.get_field('payment_status').max_length
        self.assertEqual(max_length, 30)

    def test_payment_label(self):
        payment_uuid = Payment.objects.all().first().id
        payment = Payment.objects.get(id=payment_uuid)
        field_label = payment._meta.get_field('payment_status').verbose_name
        self.assertEqual(field_label, 'payment status')

    def test_model_str(self):
        payment_uuid = Payment.objects.all().first().id
        payment = Payment.objects.get(id=payment_uuid)
        # payment_status = Payment.objects.create(payment_status="payment")
        self.assertEqual(payment.__str__(), "already paid")
