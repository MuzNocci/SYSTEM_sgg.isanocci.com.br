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
                rg=rg
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