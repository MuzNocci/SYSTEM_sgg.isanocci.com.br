from django.urls import path
from app.gallery.views import GalleriesView, GalleryView, GalleryRegister, GalleryUpdate, GalleryDelete



urlpatterns = [
    
    path('galleries/', GalleriesView.as_view(), name='galleries_view'),
    path('gallery/register/', GalleryRegister.as_view(), name='gallery_register'),
    path('gallery/<uuid:id>/', GalleryView.as_view(), name='gallery_view'),
    path('gallery/<uuid:id>/update/', GalleryUpdate.as_view(), name='gallery_update'),
    path('gallery/<uuid:id>/delete/', GalleryDelete.as_view(), name='gallery_delete'),

]