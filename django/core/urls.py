from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from common.views import Handler403View, Handler404View, Handler500View, Handler502View



urlpatterns = [

    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler403 = Handler403View.as_view()
handler404 = Handler404View.as_view()
handler500 = Handler500View.as_view()
handler502 = Handler502View.as_view()