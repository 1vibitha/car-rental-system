from django import forms
from . models import ConversationMessage
INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        widgets = {
            'content': forms.TextInput(attrs={
                'placeholder': 'Your the message',
                'class': INPUT_CLASSES,
                'style': 'width: 60%; height: 70px;',
            }),
        }