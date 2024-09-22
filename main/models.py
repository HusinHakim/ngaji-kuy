from django.db import models
from django.contrib.auth.models import User
import uuid

class Quran(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField()    
    stock = models.IntegerField(default=2) # stock quran yang tersedia
    publisher = models.CharField(max_length=255, default="No Publisher") # penerbit quran
    type = models.CharField(max_length=255, default="Tafsir") # jenis quran (quran tafsir atau quran terjemahan)
    

    @property
    def is_in_stock(self):
        return self.stock > 0
    
