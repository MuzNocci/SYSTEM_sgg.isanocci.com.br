from django import forms
from common import validators
from app.package.models import Plan, Package
from decimal import Decimal



class PlanRegisterForm(forms.Form):


    name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'id': 'name',
            'name': 'name',
            'placeholder': 'Digite o nome do plano',
            'maxlength': '255'
        }),
        error_messages={
            'required': 'O campo Nome é obrigatório.',
            'invalid': 'Insira um nome válido.'
        }
    )

    duration = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={
            'id': 'name',
            'name': 'name',
            'placeholder': 'Digite a duração do plano',
            'maxlength': '3',
            'onkeydown':'javascript: fMasc( this, isNumber );',
        }),
        error_messages={
            'required': 'O campo duração é obrigatório.',
            'invalid': 'Insira um duração válido.'
        }
    )

    price = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'id': 'price',
            'name': 'price',
            'placeholder': 'Digite o preço do plano',
            'maxlength': '10',
            'onkeydown':'javascript: fMasc( this, isMoney );',
        }),
        error_messages={
            'required': 'O campo preço é obrigatório.',
            'invalid': 'Insira um preço válido.'
        }
    )


    def clean_name(self):
        name = self.cleaned_data.get('name')
        validators.Validate.valid_name(name)
        return name
    
    def clean_duration(self):
        duration = self.cleaned_data.get('duration')
        validators.Validate.valid_duration(duration)
        return duration
    
    def clean_price(self):
        price = self.cleaned_data["price"]
        price = price.replace("R$", "").replace(".", "").replace(",", ".")
        return Decimal(price)