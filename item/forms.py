
from django import forms
from .models import Item, Category


INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'
class NewItemForm(forms.ModelForm):
    # Use a dropdown for existing categories
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={
            'class': INPUT_CLASSES,
            'style': 'width: 100%; height: 40px;',
        }),
        required=False,  # Make it optional so a new category can be added instead
        empty_label="Select Existing Category",
    )

    # Create a new text input field for adding a new category
    new_category = forms.CharField(
        required=False,  # New category is optional
        widget=forms.TextInput(attrs={
            'placeholder': 'Or Add New Category',
            'class': INPUT_CLASSES,
            'style': 'width: 100%; height: 20px;',
        })
    )

    class Meta:
        model = Item
        fields = ('category', 'new_category', 'name', 'description', 'price', 'image', 'company', 'model', 'seats', 'fuel_type', 'gear_type')

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter Item Name',
                'class': INPUT_CLASSES,
                'style': 'width: 100%; height: 20px;',
            }),
            'company': forms.TextInput(attrs={
                'placeholder': 'Enter Item Company',
                'class': INPUT_CLASSES,
                'style': 'width: 100%; height: 20px;',
            }),
            'model': forms.TextInput(attrs={
                'placeholder': 'Enter Item Model',
                'class': INPUT_CLASSES,
                'style': 'width: 100%; height: 20px;',
            }),
            'seats': forms.TextInput(attrs={
                'placeholder': 'Enter Number of Seats',
                'class': INPUT_CLASSES,
                'style': 'width: 100%; height: 20px;',
            }),
            'fuel_type': forms.TextInput(attrs={
                'placeholder': 'Enter Item Fuel Type',
                'class': INPUT_CLASSES,
                'style': 'width: 100%; height: 20px;',
            }),
            'gear_type': forms.TextInput(attrs={
                'placeholder': 'Enter Item Gear Type',
                'class': INPUT_CLASSES,
                'style': 'width: 100%; height: 20px;',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter Item Description',
                'class': INPUT_CLASSES,
                'style': 'width: 100%; height: 100px;',
            }),
            'price': forms.TextInput(attrs={
                'placeholder': 'Enter Item Price',
                'class': INPUT_CLASSES,
                'style': 'width: 100%; height: 20px;',
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES,
                'style': 'width: 100%; height: 20px;',
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        new_category = cleaned_data.get('new_category')

        # Ensure either an existing category is selected or a new category is provided
        if not category and not new_category:
            raise forms.ValidationError('Please select an existing category or add a new category.')

        return cleaned_data


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