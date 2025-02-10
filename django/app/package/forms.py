from django import forms
from common import validators
from app.client.models import Client
from app.package.models import Plan, Package
from decimal import Decimal
from datetime import date, timedelta



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
        return name
    

    def clean_duration(self):
        duration = self.cleaned_data.get('duration')
        validators.Validate.valid_duration(duration)
        return duration
    

    def clean_price(self):
        price = self.cleaned_data["price"]
        price = price.replace("R$", "").replace(".", "").replace(",", ".")
        return Decimal(price)



class PackageRegisterForm(forms.Form):


    client = forms.ChoiceField(
        required=False,
        choices=[(client.id, client.name) for client in Client.objects.all()],
        widget=forms.Select(attrs={
            'id': 'client',
            'name': 'client'
        }),
        error_messages={'required': 'O campo cliente é obrigatório.'}
    )

    plan = forms.ChoiceField(
        required=False,
        choices=[(plan.id, plan.name) for plan in Plan.objects.exclude(name__icontains="Automático")],
        widget=forms.Select(attrs={
            'id': 'plan',
            'name': 'plan'
        }),
        error_messages={'required': 'O campo plano é obrigatório.'}
    )

    created_at = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={
            'id': 'created_at',
            'name': 'created_at',
            'placeholder': 'dd/mm/aaaa',
            'type': 'date',
            'min': '1900-01-01',
            'max': date.today() + timedelta(days=30),
        }),
        error_messages={'required': 'O campo cata de criação é obrigatório.'}
    )


    def clean_client(self):
        client = self.cleaned_data.get('client')
        return client
    

    def clean_plan(self):
        plan = self.cleaned_data.get('plan')
        return plan
    

    def clean_created_at(self):
        created_at = self.cleaned_data.get('created_at')
        return created_at