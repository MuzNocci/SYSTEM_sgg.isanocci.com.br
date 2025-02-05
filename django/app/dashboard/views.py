from django.shortcuts import render
from django.views import View
from app.package.models import Package
from datetime import datetime
from dateutil.relativedelta import relativedelta



class DashboardView(View):
    

    def get(self, request):

        hoje = datetime.today()
        deadline = hoje.replace(month=hoje.month + 1)

        expired = Package.objects.filter(active=True, deadline__lt=hoje).order_by('deadline')
        expiring = Package.objects.filter(active=True, deadline__range=(hoje, deadline)).order_by('deadline')

        context = {
            'expired': expired,
            'expiring': expiring,
        }
        return render(request, 'dashboard_show.html', context)