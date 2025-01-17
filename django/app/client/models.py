import os
import uuid
from django.db import models
from common.utils import remove_chars



def unique_file_path(instance, filename):

    ext = filename.split('.')[-1]
    new_filename = f"{uuid.uuid4().hex}.{ext}"
    # upload_to = 'vol/static/app/images/clients/photos/' # Produção
    upload_to = 'static/app/images/clients/photos/' 

    while instance.__class__.objects.filter(photo=os.path.join(upload_to, new_filename)).exists():
        new_filename = f"{uuid.uuid4().hex}.{ext}"

    return os.path.join(upload_to, new_filename)


class Client(models.Model):

    GENDER = [
        ('N', 'Não informado'),
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]

    STATES = [
        ('NI', 'Não informado'),
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
        ('TO', 'Tocantins'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    photo = models.ImageField(upload_to=unique_file_path, null=True, blank=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    instagram = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=255, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)
    whatsapp = models.BooleanField(default=False)
    gender = models.CharField(max_length=1, choices=GENDER, default='N')
    birth = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    rg = models.CharField(max_length=12, null=True, blank=True)
    zip_code = models.CharField(max_length=9, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    address_number = models.CharField(max_length=6, null=True, blank=True)
    complement = models.CharField(max_length=45, null=True, blank=True)
    neighborhood = models.CharField(max_length=45, null=True, blank=True)
    city = models.CharField(max_length=45, null=True, blank=True)
    state = models.CharField(max_length=2, choices=STATES, default='NI')
    observation = models.TextField(max_length=500, null=True, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)



    def photo_filename(self):

        return os.path.basename(self.photo.name)
    
    
    def phone_number(self):

        return remove_chars('[() .,-]', self.phone)
    


    def __str__(self):

        return self.name


    def delete(self, *args, **kwargs):

        if self.photo:
            if os.path.isfile(self.photo.path):
                os.remove(self.photo.path)

        super().delete(*args, **kwargs)