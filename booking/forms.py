
from django import forms
class BookingForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)
    pincode = forms.CharField(max_length=10, required=True)
# forms.py

from django import forms

from django import forms
from django import forms

class PaymentForm(forms.Form):
    payment_method = forms.ChoiceField(
        choices=[
            ('card', 'Credit/Debit Card'),
            ('upi', 'UPI'),
        ],
        widget=forms.RadioSelect,
        label="Select Payment Method"
    )
    card_number = forms.CharField(max_length=16, required=False, label="Card Number")
    card_name = forms.CharField(max_length=100, required=False, label="Name on Card")
    cvv = forms.CharField(max_length=3, required=False, label="CVV")
    expiry_date = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'datepicker', 'placeholder': 'MM/YY'}),
        label="Expiry Date (MM/YY)"
    )
    upi_id = forms.CharField(max_length=100, required=False, label="UPI ID")
