# forms.py


from django import forms
from .models import Order
class CartItemForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)

class CheckoutForm1(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)
    address_street = forms.CharField(max_length=255)
    address_optional = forms.CharField(max_length=255, required=False)
    town_city = forms.CharField(max_length=100)
    country_state = forms.CharField(max_length=100)
    postcode_zip = forms.CharField(max_length=20)
    phone = forms.CharField(max_length=20)
    email = forms.EmailField()
    create_account = forms.BooleanField(required=False)
    account_password = forms.CharField(widget=forms.PasswordInput(), required=False)
    note = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), required=False)
    
class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name','last_name','country','address_street','address_optional','town_city','postcode_zip','phone','email','create_account','account_password','note']