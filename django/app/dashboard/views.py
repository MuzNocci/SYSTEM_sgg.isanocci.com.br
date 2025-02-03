from django.shortcuts import render
from django.views import View
from app.package.models import Package
from datetime import datetime
from dateutil.relativedelta import relativedelta



class DashboardView(View):

    def get(self, request):

        hoje = datetime.today()
        primeiro_dia_proximo_mes = hoje.replace(day=1) + relativedelta(months=1)
        ultimo_dia_proximo_mes = primeiro_dia_proximo_mes + relativedelta(day=31)

        expired = Package.objects.filter(active=True, deadline__lte=hoje).order_by('deadline')
        expiring = Package.objects.filter(active=True, deadline__gte=hoje, deadline__lte=ultimo_dia_proximo_mes).order_by('deadline')

        context = {
            'expired': expired,
            'expiring:': expiring,

        }
        return render(request, 'dashboard_show.html', context)