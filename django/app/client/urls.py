from django.urls import path
from app.client.views import ClientsView, ClientRegister, ClientShow, ClientDelete



urlpatterns = [
    
    path('clients/', ClientsView.as_view(), name='clients_show'),
    path('client/register/', ClientRegister.as_view(), name='client_register'),
    path('client/<uuid:id>', ClientShow.as_view(), name='client_show'),
    path('client/<uuid:id>/update/', ClientShow.as_view(), name='client_update'),
    path('client/<uuid:id>/delete/', ClientDelete.as_view(), name='client_delete'),

]