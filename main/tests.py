from django.test import TestCase, Client
from django.utils import timezone
from .models import Quran

class KuyNgajiTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/halaman-tidak-ada/')
        self.assertEqual(response.status_code, 404)

    def test_quran_in_stock(self):
        now = timezone.now()
        quran = Quran.objects.create(
          name="Al-Qur'an Tajwid dan Terjemahan",
          price=120000,
          description="Al-Qur'an dengan tajwid berwarna dan terjemahan lengkap.",
          stock=10,

        )
        self.assertTrue(quran.is_in_stock)  
         