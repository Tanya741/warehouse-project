from django import forms
from .models import Product

class ProductForm(forms.Form):
     name = forms.CharField(max_length=255)
     description = forms.CharField(widget=forms.Textarea)
     category = forms.CharField(max_length=100)
     price = forms.DecimalField(max_digits=10, decimal_places=2)
     brand = forms.CharField(max_length=100, required=False)
     quantity = forms.IntegerField()


class CategoryForm(forms.Form):
     title= forms.CharField(max_length=50)
     description = forms.CharField(widget=forms.Textarea)
    # class Meta:
       
        # model = Product
        # fields = ('name', 'description', 'category', 'price', 'brand', 'quantity')
        