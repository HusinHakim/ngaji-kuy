from django.forms import ModelForm
from main.models import Quran

class QuranForm(ModelForm):
    class Meta:
        model = Quran
        fields = ["name", "price", "description", "publisher", "stock", "type"]