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



class GalleriesView(LoginRequiredMixin, View):


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
    


class GalleryView(LoginRequiredMixin, View):


    def get(self, request, id):

        gallery = get_object_or_404(Gallery, id=id)
        form = GalleryForm(update_gallery=gallery, initial={
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
        return render(request, 'gallery_show.html', context)



class GalleryRegister(LoginRequiredMixin, View):
    

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

            created_at = date.today()

            pack = request.POST.get('package')
            if pack == 'new':

                plan = Plan.objects.get(name='Automático')

                search_pack = Package.objects.filter(client=client, deadline__gte=created_at+timedelta(days=plan.duration)).exclude(plan__name="Automático").first()
                if search_pack:
                    package = search_pack
                else:
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
                created_at=created_at,
                active=True,
            )

            return redirect('galleries_view')

        context = {
            'form' : form,
        }
        return render(request, 'gallery_register.html', context)



class GalleryUpdate(LoginRequiredMixin, View):


    def get(self, request, id):

        gallery = get_object_or_404(Gallery, id=id)
        form = GalleryForm(update_gallery=gallery, initial={
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
        
        form = GalleryForm(initial={
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



class GalleryDelete(LoginRequiredMixin, View):


    def get(self, request, id):

        gallery = get_object_or_404(Gallery, id=id)

        context = {
            'gallery': gallery,
        }
        return render(request, 'gallery_delete.html', context)


    def post(self, request, id):

        gallery = get_object_or_404(Gallery, id=id)
        same_package = Gallery.objects.filter(package=gallery.package.id).exclude(id=gallery.id)

        if not same_package:
            package = Package.objects.get(id=gallery.package.id)
            package.delete()
        else:
            gallery.delete()

        return redirect('galleries_view')