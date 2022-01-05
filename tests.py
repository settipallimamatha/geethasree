from django.test import TestCase
from.models import klmn
# Create your tests here.
class Basictests(TestCase):
    def setUp(self):
        klmn.objects.create(name='ponds',
                            description='glow in skin',
                            costperitem='500.000',
                            stockquantity='8.00',
                            volume='4000')
        def test_get_method(self):
            url = "http://127.0.01:8000/klmn/"
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            qs = klmn.objects.filter(name='ponds')
            self.assertEqual(qs.count(), 0)
