from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django import forms
from common import validators
from app.gallery.models import Gallery
from app.client.models import Client
from app.package.models import Package



class GalleryForm(forms.Form):


    client = forms.ChoiceField(
        required=False,
        choices=[(client.id, client.name) for client in Client.objects.all()],
        widget=forms.Select(attrs={
            'id': 'client',
        }),
        error_messages={'required': 'O campo cliente é obrigatório.'}
    )

    package = forms.ChoiceField(
        required=False,
        choices=[("new", "Novo pacote (Automático)")] + [(package.id, package.name) for package in Package.objects.all()],
        widget=forms.Select(attrs={
            'id': 'package',
        }),
        error_messages={'required': 'O campo pacote é obrigatório.'}
    )

    name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'id': 'name',
            'placeholder': 'Digite o nome',
            'maxlength': '255'
        }),
        error_messages={
            'required': 'O campo Nome é obrigatório.',
            'invalid': 'Insira um nome válido.'
        }
    )

    link = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'id': 'link',
            'placeholder': 'Digite o link',
            'maxlength': '255'
        }),
        error_messages={
            'required': 'O campo Link é obrigatório.',
            'invalid': 'Insira um link válido.'
        }
    )

    link_pass = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'id': 'link_pass',
            'placeholder': 'Digite a senha',
            'maxlength': '45'
        }),
        error_messages={
            'invalid': 'Insira uma senha válida.'
        }
    )

    active = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'id': 'active',
            'checked': 'checked',
        })
    )


    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Gallery.objects.filter(name=name).exists():
            raise ValidationError('Já existe uma galeria com este nome.')
        return name