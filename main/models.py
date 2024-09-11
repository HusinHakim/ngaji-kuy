from django.db import models

class Quran(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField()
    stock = models.IntegerField(default=0) # stock quran yang tersedia
    publisher = models.CharField(max_length=255) # penerbit quran
    type = models.CharField(max_length=255) # jenis quran (quran tafsir atau quran terjemahan)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00) # diskon quran


    @property
    def is_in_stock(self):
        return self.stock > 0
