from django import forms
from .models import *

class TurnirQuestionForm(forms.ModelForm):
    class Meta:
        model = TurnirQuestion
        fields = ('name_surname', 'age', 'telephone', 'text')
        widgets = {
            'name_surname': forms.TextInput(attrs={'placeholder': 'Ism Familiya: '}),
            'age': forms.NumberInput(attrs={'placeholder': 'Yosh: '}),
            'telephone': forms.TextInput(attrs={'placeholder': 'Telefon: '}),
            'text': forms.Textarea(attrs={'rows':4, 'cols':22, 'placeholder': "Qo'shimcha fikringiz: "}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name_surname'].label = ''
        self.fields['age'].label = ''
        self.fields['telephone'].label = ''
        self.fields['text'].label = ''


class TurnirAuthForm(forms.ModelForm):
    class Meta:
        model = TurnirAuth
        fields = ('name_surname', 'age', 'staj', 'telephone', 'text')
        widgets = {
            'name_surname': forms.TextInput(attrs={'placeholder': 'Ism Familiya: '}),
            'age': forms.NumberInput(attrs={'placeholder': 'Yosh: '}),
            'staj': forms.TextInput(attrs={'placeholder': 'Tajribangiz necha oy/yil ?: '}),
            'telephone': forms.TextInput(attrs={'placeholder': 'Telefon: '}),
            'text': forms.Textarea(attrs={'rows':4, 'cols':22, 'placeholder': "Qo'shimcha fikringiz: "}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name_surname'].label = ''
        self.fields['age'].label = ''
        self.fields['staj'].label = ''
        self.fields['telephone'].label = ''
        self.fields['text'].label = ''


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ism Familiya: '}),
            'phone': forms.TextInput(attrs={'placeholder': 'Telefon: '}),
            'text': forms.Textarea(attrs={'rows':4, 'cols':22, 'placeholder': "Qo'shimcha fikringiz: "}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = ''
        self.fields['phone'].label = ''
        self.fields['text'].label = ''