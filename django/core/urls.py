from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from common.views import Handler403View, Handler404View, Handler500View, Handler502View



urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('auth/', include('app.client.urls')),
    path('auth/', include('app.package.urls')),
    path('auth/', include('app.gallery.urls')),
    path('auth/', include('app.dashboard.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

handler403 = Handler403View.as_view()
handler404 = Handler404View.as_view()
handler500 = Handler500View.as_view()
handler502 = Handler502View.as_view()