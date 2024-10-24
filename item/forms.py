
from django import forms
from .models import Item, Category


INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={
            'class': INPUT_CLASSES,
            'style': 'width: 100%; height: 40px;',  # Adjusting size here
        }),
        empty_label="Select Category",  # Optional: to show placeholder
    )
    
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image', 'company', 'model', 'seats', 'fuel_type', 'gear_type')
        
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter Item Name',
                'class': INPUT_CLASSES,
                'style': 'width: 100%; height: 20px;'
            }),
            'company': forms.TextInput(attrs={
                'placeholder': 'Enter Item Company',
                'class': INPUT_CLASSES,
                'style': 'width: 100%; height: 20px;'
            }),
            'model': forms.TextInput(attrs={
                'placeholder': 'Enter Item Model',
                'class': INPUT_CLASSES,
                'style': 'width: 100%; height: 20px;'
            }),
            'seats': forms.TextInput(attrs={
                'placeholder': 'Enter Number of Seats',
                'class': INPUT_CLASSES,
                'style': 'width: 100%; height: 20px;'
            }),
            'fuel_type': forms.TextInput(attrs={
                'placeholder': 'Enter Item Fuel Type',
                'class': INPUT_CLASSES,
                'style': 'width: 100%; height: 20px;'
            }),
            'gear_type': forms.TextInput(attrs={
                'placeholder': 'Enter Item Gear Type',
                'class': INPUT_CLASSES,
                'style': 'width: 100%; height: 20px;'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter Item Description',
                'class': INPUT_CLASSES,
                'style': 'width: 100%; height: 100px;'  # Increasing height for description
            }),
            'price': forms.TextInput(attrs={
                'placeholder': 'Enter Item Price',
                'class': INPUT_CLASSES,
                'style': 'width: 100%; height: 20px;'
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES,
                'style': 'width: 100%; height: 20px;'
            }),
        }



class EditItemForm(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = ( 'name', 'description', 'price', 'image', 'company', 'model', 'seats', 'fuel_type', 'gear_type','is_sold')
        
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter Item Name',
                'class': INPUT_CLASSES,
                'style': 'width: 100%; height: 20px;'
            }),
            'company': forms.TextInput(attrs={
                'placeholder': 'Enter Item Company',
                'class': INPUT_CLASSES,
                'style': 'width: 100%; height: 20px;'
            }),
            'model': forms.TextInput(attrs={
                'placeholder': 'Enter Item Model',
                'class': INPUT_CLASSES,
                'style': 'width: 100%; height: 20px;'
            }),
            'seats': forms.TextInput(attrs={
                'placeholder': 'Enter Number of Seats',
                'class': INPUT_CLASSES,
                'style': 'width: 100%; height: 20px;'
            }),
            'fuel_type': forms.TextInput(attrs={
                'placeholder': 'Enter Item Fuel Type',
                'class': INPUT_CLASSES,
                'style': 'width: 100%; height: 20px;'
            }),
            'gear_type': forms.TextInput(attrs={
                'placeholder': 'Enter Item Gear Type',
                'class': INPUT_CLASSES,
                'style': 'width: 100%; height: 20px;'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter Item Description',
                'class': INPUT_CLASSES,
                'style': 'width: 100%; height: 100px;'  # Increasing height for description
            }),
            'price': forms.TextInput(attrs={
                'placeholder': 'Enter Item Price',
                'class': INPUT_CLASSES,
                'style': 'width: 100%; height: 20px;'
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES,
                'style': 'width: 100%; height: 20px;'
            }),
        }