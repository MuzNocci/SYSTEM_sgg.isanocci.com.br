from django.urls import path
from app.client.views import ClientsView, ClientRegister, ClientUpdate, ClientView, ClientDelete



urlpatterns = [
    
    path('clients/', ClientsView.as_view(), name='clients_view'),
    path('client/register/', ClientRegister.as_view(), name='client_register'),
    path('client/<uuid:id>', ClientView.as_view(), name='client_view'),
    path('client/<uuid:id>/update/', ClientUpdate.as_view(), name='client_update'),
    path('client/<uuid:id>/delete/', ClientDelete.as_view(), name='client_delete'),

]