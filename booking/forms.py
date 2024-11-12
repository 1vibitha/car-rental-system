from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta


class BookingForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        error_messages={'required': 'Please enter your name.'}
    )
    email = forms.EmailField(
        required=True,
        error_messages={'required': 'Please enter a valid email address.'}
    )
    phone = forms.CharField(
        max_length=15,
        required=True,
        error_messages={'required': 'Please enter your phone number.'}
    )
    address = forms.CharField(
        widget=forms.Textarea,
        required=True,
        error_messages={'required': 'Please enter your address.'}
    )
    pincode = forms.CharField(
        max_length=10,
        required=True,
        error_messages={'required': 'Please enter your pincode.'}
    )


class PaymentForm(forms.Form):
    payment_method = forms.ChoiceField(
        choices=[
            ('card', 'Credit/Debit Card'),
            ('upi', 'UPI'),
        ],
        widget=forms.RadioSelect,
        label="Select Payment Method"
    )
    card_number = forms.CharField(
        max_length=16, 
        required=False, 
        label="Card Number",
        widget=forms.TextInput(attrs={
            'maxlength': '16', 
            'inputmode': 'numeric', 
            'pattern': '[0-9]*', 
            'placeholder': 'Enter 16-digit card number'
        })
    )
    card_name = forms.CharField(max_length=100, required=False, label="Name on Card")
    cvv = forms.CharField(
        max_length=3, 
        required=False, 
        label="CVV",
        widget=forms.TextInput(attrs={
            'maxlength': '3', 
            'inputmode': 'numeric', 
            'pattern': '[0-9]*', 
            'placeholder': 'Enter 3-digit CVV'
        })
    )
    expiry_date = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'datepicker', 'placeholder': 'MM/YY'}),
        label="Expiry Date (MM/YY)"
    )
    upi_id = forms.CharField(max_length=100, required=False, label="UPI ID")

    def clean(self):
        cleaned_data = super().clean()
        payment_method = cleaned_data.get('payment_method')

        if payment_method == 'card':
            required_card_fields = ['card_number', 'card_name', 'cvv', 'expiry_date']
            missing_fields = [field for field in required_card_fields if not cleaned_data.get(field)]
            if missing_fields:
                raise ValidationError(f"Missing fields for card payment: {', '.join(missing_fields)}")

            if len(cleaned_data.get('card_number', '')) != 16:
                self.add_error('card_number', "Card number must be exactly 16 digits.")
            if len(cleaned_data.get('cvv', '')) != 3:
                self.add_error('cvv', "CVV must be exactly 3 digits.")

            expiry_date = cleaned_data.get('expiry_date', '')
            try:
                # Parse expiry date
                expiry_date_obj = datetime.strptime(expiry_date, "%m/%y")
                # Get current date
                current_date = datetime.now()
                # Set the day to the last day of the expiry month
                expiry_date_obj = expiry_date_obj.replace(day=1) + timedelta(days=31)
                expiry_date_obj = expiry_date_obj.replace(day=1) - timedelta(days=1)
                
                if expiry_date_obj < current_date:
                    self.add_error('expiry_date', "Expiry date cannot be in the past.")

            except ValueError:
                self.add_error('expiry_date', "Expiry date format must be MM/YY.")

        elif payment_method == 'upi' and not cleaned_data.get('upi_id'):
            raise ValidationError("UPI ID is required for UPI payment.")

        return cleaned_data
