from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from app.package.models import Package
from app.gallery.models import Gallery
from app.client.models import Client
from datetime import datetime
from dateutil.relativedelta import relativedelta



class DashboardView(LoginRequiredMixin, View):
    

    def get(self, request):

        hoje = datetime.today()
        deadline = hoje + relativedelta(months=1)

        expired = Package.objects.filter(active=True, deadline__lt=hoje).order_by('deadline')
        expiring = Package.objects.filter(active=True, deadline__range=(hoje, deadline)).order_by('deadline')

        context = {
            'expired': expired,
            'expiring': expiring,
            'clients': Client.objects.all().count() or 0,
            'packages': Package.objects.all().count() or 0,
            'galleries': Gallery.objects.all().count() or 0,
            # 'values': 'R$ 0,00'
        }
        return render(request, 'dashboard_show.html', context)