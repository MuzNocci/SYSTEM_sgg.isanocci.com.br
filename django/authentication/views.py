from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views import View



class LoginView(View):


    def get(self, request):

        return render(request, 'login.html')
    

    def post(self, request):

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard_view")
        else:
            messages.error(request, "Usuário ou senha inválidos")

        return render(request, "login.html")