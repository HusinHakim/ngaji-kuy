from django.forms import ModelForm
from main.models import Quran
from django.utils.html import strip_tags

from django.core.exceptions import ValidationError

class QuranForm(ModelForm):
    class Meta:
        model = Quran
        fields = ["name", "price", "description", "publisher", "stock", "type"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        name = strip_tags(name)
        if not name:
            raise ValidationError("Nama tidak boleh kosong.")
        return name

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)

    def clean_publisher(self):
        publisher = self.cleaned_data["publisher"]
        return strip_tags(publisher)

    def clean_type(self):
        type_field = self.cleaned_data["type"]
        return strip_tags(type_field)
