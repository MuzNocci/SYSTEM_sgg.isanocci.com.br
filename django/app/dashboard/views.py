from django.shortcuts import render
from django.views import View



class DashboardView(View):

    def get(self, request):

        context = {
        }
        return render(request, 'dashboard_show.html', context)