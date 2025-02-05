from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.core.paginator import Paginator
from app.package.models import Plan
from app.package.forms import PlanRegisterForm
from django.shortcuts import render, redirect



class PlansView(LoginRequiredMixin, View):


    def get(self, request):


        plans = Plan.objects.all().order_by('name')

        context = {
            'plans': plans,
        }
        return render(request, 'plans_show.html', context)
    

class PlanRegister(LoginRequiredMixin, View):


    def get(self, request):

        form = PlanRegisterForm()

        context = {
            'form' : form,
        }
        return render(request, 'plan_register.html', context)
    

    def post(self, request):

        form = PlanRegisterForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            duration = form.cleaned_data.get('duration')
            price = form.cleaned_data.get('price')
        
            Plan.objects.create(
                name=name, 
                duration=duration, 
                price=price
            )

            return redirect('plans_view')
        
        context = {
            'form' : form,
        }
        return render(request, 'plan_register.html', context)
    

class PlanUpdate(LoginRequiredMixin, View):


    def get(self, request, id):

        plan = Plan.objects.get(id=id)
        form = PlanRegisterForm(initial={
            'name': plan.name,
            'duration': plan.duration,
            'price': 'R$ ' + str(plan.price).replace('.', ',')
        })

        context = {
            'form' : form,
            'plan' : plan
        }
        return render(request, 'plan_update.html', context)
    

    def post(self, request, id):

        plan = Plan.objects.get(id=id)
        form = PlanRegisterForm(request.POST)

        if form.is_valid():
            plan.name = form.cleaned_data.get('name')
            plan.duration = form.cleaned_data.get('duration')
            plan.price = form.cleaned_data.get('price')
            plan.save()

            return redirect('plans_view')
        
        context = {
            'form' : form,
            'plan' : plan
        }
        return render(request, 'plan_update.html', context)