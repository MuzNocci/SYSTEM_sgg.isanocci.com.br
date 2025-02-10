from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.db.models import Q
from django.core.paginator import Paginator
from app.client.models import Client
from app.package.models import Plan, Package
from app.package.forms import PlanRegisterForm, PackageRegisterForm
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, timedelta
from django.utils.dateformat import DateFormat



# Plans
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
    


class PlanDelete(LoginRequiredMixin, View):


    def get(self, request, id):

        plan = get_object_or_404(Plan, id=id)

        context = {
            'plan': plan
        }
        return render(request, 'plan_delete.html', context)
    

    def post(self, request, id):

        plan = get_object_or_404(Plan, id=id)
        plan.delete()

        return redirect('plans_view')
    


# Packages
class PackagesView(LoginRequiredMixin, View):


    def get(self, request):

        search = request.GET.get('search', '')

        if search:
            packages = Package.objects.filter(Q(plan__name__icontains=search) | Q(client__name__icontains=search)).order_by('deadline')
        else:
            packages = Package.objects.all().order_by('deadline')

        paginator = Paginator(packages, 25)
        page_number = request.GET.get('page', 1)
        packages = paginator.get_page(page_number)

        context = {
            'packages': packages,
            'search': search,
        }
        return render(request, 'packages_show.html', context)



class PackageRegister(LoginRequiredMixin, View):


    def get(self, request):

        form = PackageRegisterForm()

        context = {
            'form' : form,
        }
        return render(request, 'package_register.html', context)
    

    def post(self, request):

        form = PackageRegisterForm(request.POST)

        if form.is_valid():
            client_id = form.cleaned_data.get('client')
            client = Client.objects.get(id=client_id)
            
            plan_id = form.cleaned_data.get('plan')
            plan = Plan.objects.get(id=plan_id)
            
            created_at = form.cleaned_data.get('created_at')
            deadline = created_at + timedelta(days=plan.duration)
        
            Package.objects.create(
                client=client,
                plan=plan,
                created_at=created_at,
                deadline=deadline,
                active=True,
            )

            # Criar aqui a lógica das galerias de fotos que estiverem em um plano com vencimento anteiror.

            return redirect('packages_view')
        
        context = {
            'form' : form,
        }
        return render(request, 'package_register.html', context)
    


class PackageUpdate(LoginRequiredMixin, View):


    def get(self, request, id):

        package = get_object_or_404(Package, id=id)
        form = PackageRegisterForm(initial={
            'client': package.client.id,
            'plan': package.plan.id,
            'created_at': DateFormat(package.created_at).format('Y-m-d'),
        })

        context = {
            'form' : form,
            'package' : package,
        }
        return render(request, 'package_update.html', context)


    def post(self, request, id):

        package = get_object_or_404(Package, id=id)
        form = PackageRegisterForm(request.POST)

        if form.is_valid():

            package.client = Client.objects.get(id=form.cleaned_data.get('client'))
            package.plan = Plan.objects.get(id=form.cleaned_data.get('plan'))

            created_at = form.cleaned_data.get('created_at')
            deadline = created_at + timedelta(days=package.plan.duration)
            
            package.created_at = created_at
            package.deadline = deadline
            package.save()

            return redirect('packages_view')
        
        context = {
            'form' : form,
            'package' : package
        }
        return render(request, 'package_update.html', context)
    


class PackageDelete(LoginRequiredMixin, View):


    def get(self, request, id):

        package = get_object_or_404(Package, id=id)

        context = {
            'package': package,
        }
        return render(request, 'package_delete.html', context)


    def post(self, request, id):

        package = get_object_or_404(Package, id=id)
        package.delete()

        return redirect('packages_view')