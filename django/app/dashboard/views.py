from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from app.package.models import Package
from app.gallery.models import Gallery
from app.client.models import Client
from datetime import datetime



class DashboardView(LoginRequiredMixin, View):
    

    def get(self, request):

        hoje = datetime.today()
        deadline = hoje.replace(month=hoje.month + 1)

        expired = Package.objects.filter(active=True, deadline__lt=hoje).order_by('deadline')
        expiring = Package.objects.filter(active=True, deadline__range=(hoje, deadline)).order_by('deadline')

        context = {
            'expired': expired,
            'expiring': expiring,
            'clients': Client.objects.all().count(),
            'packages': Package.objects.all().count(),
            'galleries': Gallery.objects.all().count(),
            # 'values': 'R$ 0,00'
        }
        return render(request, 'dashboard_show.html', context)