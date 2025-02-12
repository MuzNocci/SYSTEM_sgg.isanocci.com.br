from datetime import timedelta, date
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.core.paginator import Paginator
from app.gallery.models import Gallery
from app.gallery.forms import GalleryForm
from app.client.models import Client
from app.package.models import Package, Plan



class GalleriesView(View, ):


    def get(self, request):


        search = request.GET.get('search', '')

        if search:
            galleries = Gallery.objects.filter(Q(client__name__icontains=search) | Q(name__icontains=search)).order_by('created_at')
        else:
            galleries = galleries = Gallery.objects.all().order_by('created_at')

        paginator = Paginator(galleries, 25)
        page_number = request.GET.get('page', 1)
        galleries = paginator.get_page(page_number)

        context = {
            'galleries': galleries,
        }
        return render(request, 'galleries_show.html', context)
    


class GalleryView(View):


    ...



class GalleryRegister(View):
    

    def get(self, request):

        form = GalleryForm()

        context = {
            'form' : form,
        }
        return render(request, 'gallery_register.html', context)
   

    def post(self, request):

        form = GalleryForm(request.POST)

        if form.is_valid():

            client_id = form.cleaned_data.get('client')
            client = Client.objects.get(id=client_id)

            pack = request.POST.get('package')
            if pack == 'new':
                plan = Plan.objects.get(name='Automático')
                created_at = date.today()
                package = Package.objects.create(
                    client=client,
                    plan=plan,
                    created_at=created_at,
                    deadline=created_at + timedelta(days=plan.duration),
                    active=True,
                )

            else:
                package_id = form.cleaned_data.get('package')
                package = Package.objects.get(id=package_id)

            Gallery.objects.create(
                client=client,
                package=package,
                name=form.cleaned_data.get('name'),
                link=form.cleaned_data.get('link'),
                link_pass=form.cleaned_data.get('link_pass'),
                created_at=date.today(),
                active=True,
            )

            return redirect('galleries_view')

        context = {
            'form' : form,
        }
        return render(request, 'gallery_register.html', context)



class GalleryUpdate(View):


    def get(self, request, id):

        gallery = get_object_or_404(Gallery, id=id)
        form = GalleryForm(exclude_option=True, initial={
            'client': gallery.client.id,
            'package': gallery.package.id,
            'name': gallery.name,
            'link': gallery.link,
            'link_pass': gallery.link_pass,
            'active': gallery.active,
        })

        context = {
            'gallery': gallery,
            'form' : form,
        }
        return render(request, 'gallery_update.html', context)
   

    def post(self, request, id):

        gallery = get_object_or_404(Gallery, id=id)
        form = GalleryForm(request.POST)

        if form.is_valid():

            gallery.client = Client.objects.get(id=form.cleaned_data.get('client'))
            gallery.package = Package.objects.get(id=form.cleaned_data.get('package'))
            gallery.name = form.cleaned_data.get('name')
            gallery.link = form.cleaned_data.get('link')
            gallery.link_pass = form.cleaned_data.get('link_pass')
            gallery.created_at = date.today()
            gallery.active = form.cleaned_data.get('active')
            gallery.save()


            return redirect('galleries_view')
        
        form = GalleryForm(exclude_option=True, initial={
            'client': gallery.client.id,
            'package': gallery.package.id,
            'name': gallery.name,
            'link': gallery.link,
            'link_pass': gallery.link_pass,
            'active': gallery.active,
        })

        context = {
            'gallery': gallery,
            'form' : form,
        }
        return render(request, 'gallery_update.html', context)



class GalleryDelete(View):

    ... 