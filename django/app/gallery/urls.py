from django.urls import path
from app.gallery.views import GalleryView



urlpatterns = [
    
    path('gallerys/', GalleryView.as_view(), name='gallerys_view'),
    # path('gallery/register/', GalleryRegister.as_view(), name='gallery_register'),
    # path('gallery/<uuid:id>/update/', GalleryUpdate.as_view(), name='gallery_update'),
    # path('gallery/<uuid:id>/delete/', GalleryDelete.as_view(), name='gallery_delete'),

]