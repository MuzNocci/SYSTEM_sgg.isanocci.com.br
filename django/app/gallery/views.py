from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from app.gallery.models import Gallery



class GalleryView(View):


    def get(self, request):

        galleries = Gallery.objects.all().order_by('name')

        context = {
            'galleries': galleries,
        }
        return render(request, 'galleries_show.html', context)