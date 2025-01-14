from django.shortcuts import render
from django.views import View
from app.client.models import Client



class ClientView(View):


    def get(self, request):

        client = Client.objects.all().order_by('name')

        context = {
            'clients': client,
        }
        return render(request, 'clients_show.html', context)
    

    def post(self, request):

        client = Client.objects.filter(name__icontains=request.POST['search']).order_by('name')

        context = {
            'clients': client,
        }
        return render(request, 'clients_show.html', context)