from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    # adds classes and place holders and labels
    title = forms.CharField(label='Product',widget=forms.TextInput(attrs={"placeholder": "Product Name",
                                                    "class":"form-control"}))
    price = forms.DecimalField(label='Price',widget=forms.NumberInput(attrs={"placeholder": "00.00",
                                                    "class":"form-control"}))
    quantity = forms.IntegerField(label='Quantity',widget=forms.NumberInput(attrs={"placeholder": "0",
                                                    "class":"form-control"}))
    date = forms.DateField(label='Expiration Date',input_formats=['%m/%d/%y'],widget=forms.DateInput(attrs={
                                                "placeholder":"mm-dd-yy"
                                            }))
    # What fields the form will create 
    class Meta:
        model = Product
        fields =[
            "title",
            "price",
            "quantity",
            "available",
            "date"
        ]


                                                   
