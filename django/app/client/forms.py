from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django import forms


class ClientRegisterForm(forms.Form):

    name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'id': 'name',
            'name': 'name',
            'class': '',
            'placeholder': 'Digite o nome',
            'maxlength':'255'
        }),
        error_messages={
            'required': 'O campo Nome é obrigatório.',
            'invalid': 'Insira um nome válido.'
        }
    )

    instagram = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'id': 'instagram',
            'name': 'instagram',
            'placeholder': '@instagram',
            'maxlengh':'30',
        })
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'id': 'email',
            'name': 'email',
            'placeholder': 'Digite o email',
            'maxlength':'255'
        }),
        error_messages={
            'required': 'O campo Email é obrigatório.',
            'invalid': 'Insira um email válido.'
        }
    )

    phone = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'id': 'phone',
            'name': 'phone',
            'placeholder': '(22) 99999-9999',
            'maxlength':'15',
        }),
        error_messages={'required': 'O campo Celular é obrigatório.'}
    )

    whatsapp = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'id': 'whatsapp', 'name': 'whatsapp'})
    )

    gender = forms.ChoiceField(
        required=False,
        choices=[('', '-- Selecione --'), ('M', 'Masculino'), ('F', 'Feminino')],
        widget=forms.Select(attrs={
            'id': 'gender',
            'name': 'gender',
        }),
    )

    birth = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'id': 'birth',
            'name': 'birth',
            'placeholder': 'dd/mm/aaaa',
            'type': 'date',
            'maxlength':'10'
        }),
        error_messages={'required': 'O campo Data de Nascimento é obrigatório.'}
    )

    cpf = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'id': 'cpf',
            'name': 'cpf',
            'placeholder': '999.999.999-99',
            'maxlength':'14'
        }),
        error_messages={'required': 'O campo CPF é obrigatório.'}
    )

    rg = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'id': 'rg',
            'name': 'rg',
            'placeholder': '99.999.999-6',
            'maxlength':'12'
        }),
        error_messages={'required': 'O campo RG é obrigatório.'}
    )

    zip_code = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'id': 'zip_code',
            'name': 'zip_code',
            'placeholder': '00000-000',
            'maxlength':'9',
        }),
        error_messages={'required': 'O campo CEP é obrigatório.'}
    )

    address = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'id': 'address',
            'name': 'address',
            'placeholder': 'Digite o endereço (Ex: Rua Fulano de Tal)',
            'maxlength':'255',
        }),
        error_messages={'required': 'O campo Endereço é obrigatório.'}
    )

    address_number = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'id': 'address_number',
            'name': 'address_number',
            'placeholder': 'Digite o número',
            'maxlength':'6',
        }),
        error_messages={'required': 'O campo Número é obrigatório.'}
    )

    complement = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'id': 'complement',
            'name': 'complement',
            'placeholder': 'Digite o complemento do endereço',
            'maxlength':'255',
        })
    )

    district = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'id': 'district',
            'name': 'district',
            'placeholder': 'Digite o bairro',
            'maxlength':'45',
        }),
        error_messages={'required': 'O campo Bairro é obrigatório.'}
    )

    city = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'id': 'city',
            'name': 'city',
            'placeholder': 'Digite a cidade',
            'maxlength':'45',
        }),
        error_messages={'required': 'O campo Cidade é obrigatório.'}
    )

    state = forms.ChoiceField(
        required=False,
        choices=[('', '-- Selecione o Estado --'), ('SP', 'São Paulo'), ('RJ', 'Rio de Janeiro'), ('MG', 'Minas Gerais')],
        widget=forms.Select(attrs={
            'id': 'state',
            'name': 'state'
        }),
        error_messages={'required': 'O campo Estado é obrigatório.'}
    )

    observation = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'id': 'observation',
            'name': 'observation',
            'placeholder': 'Digite uma observação',
            'rows': 5,
            'maxlength':'500',
        })
    )

    active = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'id': 'active', 'name': 'active'})
    )


    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if len(cpf) != 14:
            raise forms.ValidationError('CPF inválido.')
        return cpf

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) != 14:
            raise forms.ValidationError('Número de celular inválido.')
        return phone