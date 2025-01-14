from django.views import View
from django.shortcuts import render



class Handler404View(View):

    def get(self, request, exception):

        context = {
            'status':'Error',
            'statuscode':'404',
            'statustext':'Page not found',
        }
        return render(request, 'errors.html', context, status=404)
    

class Handler403View(View):

    def get(self, request, exception):

        context = {
            'status':'Error',
            'statuscode':'403',
            'statustext':'Forbidden',
        }
        return render(request, 'errors.html', context, status=403)
    

class Handler500View(View):

    def get(self, request, exception):

        context = {
            'status':'Error',
            'statuscode':'500',
            'statustext':'Internal server error',
        }
        return render(request, 'errors.html', context, status=500)
    

class Handler502View(View):

    def get(self, request, exception):

        context = {
            'status':'Error',
            'statuscode':'502',
            'statustext':'Bad gateway',
        }
        return render(request, 'errors.html', context, status=502)