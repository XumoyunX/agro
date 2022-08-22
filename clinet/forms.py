from django import forms
from main.models import News, Gallery, Pdf, Product, Send


class NewsForm(forms.ModelForm):
    class Meta:
        model = News()
        fields = '__all__'


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery()
        fields = '__all__'


class PdfForm(forms.ModelForm):
    class Meta:
        model = Pdf()
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product()
        fields = "__all__"


class SendForm(forms.ModelForm):
    class Meta:
        model = Send()
        fields = '__all__'
