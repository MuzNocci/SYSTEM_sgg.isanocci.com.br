from django.contrib import admin
from app.client.models import Client



from django.contrib import admin
from .models import Client

# Classe para customizar a exibição do modelo Client no admin
class ClientAdmin(admin.ModelAdmin):
    # Campos que serão exibidos na lista de clientes no admin
    list_display = ('name', 'email', 'cpf', 'created_at','active')
    
    # Campos que podem ser usados para busca
    search_fields = ('name', 'email', 'cpf')
    
    # Filtros para facilitar a pesquisa
    list_filter = ('active', 'gender')
    
    # Campos editáveis diretamente na listagem
    list_editable = ('active',)
    
    # # Campos que serão exibidos no detalhe do cliente
    # fields = (
    #     'name', 
    #     'email', 
    #     'cpf', 
    #     'rg', 
    #     'birth', 
    #     'gender', 
    #     'phone', 
    #     'whatsapp', 
    #     'address', 
    #     'city', 
    #     'state', 
    #     'zip_code', 
    #     'observation',
    #     'active',
    #     'created_at'
    # )
    
    # Organização em seções (opcional)
    fieldsets = (
        ('Dados Pessoais', {
            'fields': ('photo', 'name', 'email', 'cpf', 'rg', 'birth', 'gender'),
        }),
        ('Contato', {
            'fields': ('phone', 'whatsapp'),
        }),
        ('Endereço', {
            'fields': ('address', 'address_number', 'complement', 'neighborhood', 'city', 'state', 'zip_code'),
        }),
        ('Outros dados', {
            'fields': ('observation', 'active'),
        }),
    )

# Registrar o modelo Client e sua configuração no admin
admin.site.register(Client, ClientAdmin)