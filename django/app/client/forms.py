from django import forms
from common import validators
from app.client.models import Client, remove_chars



class ClientRegisterForm(forms.ModelForm):


    class Meta:
        model = Client
        fields = '__all__'


    photo = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'id': 'photo',
            'accept': 'image/*'
        }),
        error_messages={
            'invalid': 'Insira uma imagem válida.'
        }
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

    instagram = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'id': 'instagram',
            'placeholder': '@instagram',
            'maxlength': '30'
        })
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'id': 'email',
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
            'placeholder': '(22) 99999-9999',
            'maxlength':'15',
            'onkeydown':'javascript: fMasc( this, mPHONE );',
        }),
        error_messages={'required': 'O campo Celular é obrigatório.'}
    )

    whatsapp = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'id': 'whatsapp',
            'style': 'margin-top: 10px'
        })
    )

    gender = forms.ChoiceField(
        required=False,
        choices=[('N', '-- Selecione --'), ('M', 'Masculino'), ('F', 'Feminino')],
        widget=forms.Select(attrs={
            'id': 'gender',
        }),
    )

    birth = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'id': 'birth',
            'placeholder': 'dd/mm/aaaa',
            'type': 'date',
            'maxlength':'10',
        }),
        error_messages={'required': 'O campo Data de Nascimento é obrigatório.'}
    )

    cpf = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'id': 'cpf',
            'placeholder': '999.999.999-99',
            'maxlength':'14',
            'onkeydown':'javascript: fMasc( this, mCPF );',
        }),
        error_messages={'required': 'O campo CPF é obrigatório.'}
    )

    rg = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'id': 'rg',
            'placeholder': '99.999.999-6',
            'maxlength':'12',
            'onkeydown':'javascript: fMasc( this, mRG );',
        }),
        error_messages={'required': 'O campo RG é obrigatório.'}
    )

    zip_code = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'id': 'zip_code',
            'placeholder': '00000-000',
            'maxlength':'9',
            'onkeydown':'javascript: fMasc( this, mCEP );',
        }),
        error_messages={'required': 'O campo CEP é obrigatório.'}
    )

    address = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'id': 'address',
            'placeholder': 'Digite o endereço (Ex: Rua Fulano de Tal)',
            'maxlength':'255',
        }),
        error_messages={'required': 'O campo Endereço é obrigatório.'}
    )

    address_number = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'id': 'address_number',
            'placeholder': 'Digite o número',
            'maxlength':'6',
            'onkeydown':'javascript: fMasc( this, isNumber );',
        }),
        error_messages={'required': 'O campo Número é obrigatório.'}
    )

    complement = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'id': 'complement',
            'placeholder': 'Digite o complemento do endereço',
            'maxlength':'255',
        })
    )

    neighborhood = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'id': 'neighborhood',
            'placeholder': 'Digite o bairro',
            'maxlength':'45',
        }),
        error_messages={'required': 'O campo Bairro é obrigatório.'}
    )

    city = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'id': 'city',
            'placeholder': 'Digite a cidade',
            'maxlength':'45',
        }),
        error_messages={'required': 'O campo Cidade é obrigatório.'}
    )

    state = forms.ChoiceField(
        required=False,
        choices=[
            ('NI', '-- Selecione o Estado --'),
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins')
        ],
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
            'placeholder': 'Digite uma observação',
            'rows': 5,
            'maxlength':'500',
        })
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
        validators.Validate.valid_name(name)
        return name
    

    def clean_email(self):
        email = self.cleaned_data.get('email')
        validators.Validate.valid_email(email)
        return email


    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) < 14:
            raise forms.ValidationError('Telefone inválido.')
        return phone
    
    def clean_birth(self):
        birth = self.cleaned_data.get('birth')
        validators.Validate.valid_date(birth)
        return birth
    
    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if cpf:
            if Client.objects.exclude(id=self.instance.id).filter(cpf=cpf).exists():
                raise forms.ValidationError('CPF já está cadastrado.')
            else:
                validators.Validate.valid_cpf(cpf)
        return cpf

    def clean_rg(self):
        rg = self.cleaned_data.get('rg')
        if rg:
            if len(rg) != 12:
                raise forms.ValidationError('RG inválido.')
            if not remove_chars('[., -]', rg).isnumeric():
                raise forms.ValidationError('RG inválido.')
        return rg