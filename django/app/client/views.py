from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from app.client.models import Client
from app.client.forms import ClientRegisterForm



class ClientsView(View):


    def get(self, request):

        clients = Client.objects.all().order_by('name')

        context = {
            'clients': clients,
        }
        return render(request, 'clients_show.html', context)
    

    def post(self, request):

        clients = Client.objects.filter(name__icontains=request.POST['search']).order_by('name')

        context = {
            'clients': clients,
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
            
            return redirect('clients_show')

        context = {
            'form': form
        }
        return render(request, 'client_register.html', context)
    


class ClientShow(View):


    def get(self, request, id):

        client = get_object_or_404(Client, id=id)

        context = {
            'client': client
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

        return redirect('clients_show')