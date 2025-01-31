import os
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from app.client.models import Client
from app.client.forms import ClientRegisterForm
from django.db.models import Q
from django.core.paginator import Paginator



class ClientsView(View):


    def get(self, request):

        search = request.GET.get('search', '')

        if search:
            clients = Client.objects.filter(Q(name__icontains=search) | Q(phone__icontains=search)).order_by('name')
        else:
            clients = Client.objects.all().order_by('name')

        paginator = Paginator(clients, 25)
        page_number = request.GET.get('page', 1)
        clients = paginator.get_page(page_number)

        context = {
            'clients': clients,
            'search': search,
        }
        return render(request, 'clients_show.html', context)
    
    

class ClientRegister(View):


    def get(self, request):

        form = ClientRegisterForm()

        context = {
            'form' : form,
        }
        return render(request, 'client_register.html', context)
    

    def post(self, request):

        form = ClientRegisterForm(request.POST, request.FILES)

        if form.is_valid():
            photo = form.cleaned_data.get('photo')
            name = form.cleaned_data.get('name')
            instagram = form.cleaned_data.get('instagram')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            whatsapp = form.cleaned_data.get('whatsapp')
            gender = form.cleaned_data.get('gender')
            birth = form.cleaned_data.get('birth')
            cpf = form.cleaned_data.get('cpf')
            rg = form.cleaned_data.get('rg')
            zip_code = form.cleaned_data.get('zip_code')
            address = form.cleaned_data.get('address')
            address_number = form.cleaned_data.get('address_number')
            complement = form.cleaned_data.get('complement')
            neighborhood = form.cleaned_data.get('neighborhood')
            city = form.cleaned_data.get('city')
            state = form.cleaned_data.get('state')
            observation = form.cleaned_data.get('observation')
            active = form.cleaned_data.get('active')
            
            Client.objects.create(
                photo=photo,
                name=name,
                instagram=instagram,
                email=email,
                phone=phone,
                whatsapp=whatsapp,
                gender=gender,
                birth=birth,
                cpf=cpf,
                rg=rg,
                zip_code = zip_code,
                address = address,
                address_number = address_number,
                complement = complement,
                neighborhood = neighborhood,
                city = city,
                state = state,
                observation = observation,
                active = active,
            )
            
            return redirect('clients_view')

        context = {
            'form': form
        }
        return render(request, 'client_register.html', context)
    

class ClientUpdate(View):


    def get(self, request, id):

        client = get_object_or_404(Client, id=id)
        form = ClientRegisterForm(initial={
            'photo': client.photo,
            'name': client.name,
            'instagram': client.instagram,
            'email': client.email,
            'phone': client.phone,
            'whatsapp': client.whatsapp,
            'gender': client.gender,
            'birth': client.birth,
            'cpf': client.cpf,
            'rg': client.rg,
            'zip_code': client.zip_code,
            'address': client.address,
            'address_number': client.address_number,
            'complement': client.complement,
            'neighborhood': client.neighborhood,
            'city': client.city,
            'state': client.state,
            'observation': client.observation,
            'active': client.active,
        })

        context = {
            'client': client,
            'form' : form,
        }
        return render(request, 'client_update.html', context)
    

    def post(self, request, id):

        client = get_object_or_404(Client, id=id)
        form = ClientRegisterForm(request.POST, request.FILES)

        if form.is_valid():

            new_photo = form.cleaned_data.get('photo')

            if new_photo and client.photo and client.photo != new_photo:
                if os.path.isfile(client.photo.path):
                    os.remove(client.photo.path)

            for field, value in form.cleaned_data.items():
                if value:
                    setattr(client, field, value)

            client.save()
            
            return redirect('clients_view')

        context = {
            'client': client,
            'form': form,
        }
        return render(request, 'client_update.html', context)


class ClientView(View):


    def get(self, request, id):

        client = get_object_or_404(Client, id=id)
        form = ClientRegisterForm(initial={
            'name': client.name,
            'instagram': client.instagram,
            'email': client.email,
            'phone': client.phone,
            'whatsapp': client.whatsapp,
            'gender': client.gender,
            'birth': client.birth,
            'cpf': client.cpf,
            'rg': client.rg,
            'zip_code': client.zip_code,
            'address': client.address,
            'address_number': client.address_number,
            'complement': client.complement,
            'neighborhood': client.neighborhood,
            'city': client.city,
            'state': client.state,
            'observation': client.observation,
            'active': client.active,
        })
        

        context = {
            'client': client,
            'form' : form,
        }
        return render(request, 'client_show.html', context)
    


class ClientDelete(View):


    def get(self, request, id):

        client = get_object_or_404(Client, id=id)

        context = {
            'client': client
        }
        return render(request, 'client_delete.html', context)
    

    def post(self, request, id):

        client = get_object_or_404(Client, id=id)
        client.delete()

        return redirect('clients_view')