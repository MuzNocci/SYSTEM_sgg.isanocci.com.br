from django import forms
from app.client.models import Client
from app.package.models import Package



class GalleryForm(forms.Form):


    client = forms.ChoiceField(
        required=False,
        widget=forms.Select(attrs={
            'id': 'client',
        }),
        error_messages={'required': 'O campo cliente é obrigatório.'}
    )

    package = forms.ChoiceField(
        required=False,
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
        })
    )
    

    def __init__(self, *args, update_gallery=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['client'].choices=[(client.id, client.name) for client in Client.objects.all()]

        if update_gallery:
            if update_gallery.package.plan.name == 'Automático':
                self.fields['package'].choices = [(update_gallery.package.id, update_gallery.package.name)] + [(package.id, package.name) for package in Package.objects.filter(client=update_gallery.client).exclude(plan__name='Automático', id=update_gallery.package.id)]
            else:
                self.fields['package'].choices = [(package.id, package.name) for package in Package.objects.filter(client=update_gallery.client).exclude(plan__name='Automático')]
        else:   
            self.fields['package'].choices = [("new", "Novo pacote (Automático)")] + [(package.id, package.name) for package in Package.objects.exclude(plan__name='Automático')]
