from django.test import TestCase
from customer.models import Customer

# Create your tests here.

class CustomerTestCase(TestCase):
    def setUp(self):
        self.maxDiff = None
        a_customer = Customer.objects.create(
            password='123456',
            user_name='sysuye'
        )
