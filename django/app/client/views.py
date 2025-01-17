from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from app.client.models import Client



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

        return render(request, 'client_register.html')
    

    def post(self, request):

        form = request.POST

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