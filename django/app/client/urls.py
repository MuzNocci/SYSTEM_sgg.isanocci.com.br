from django.urls import path
from app.client.views import ClientView, ClientRegister



urlpatterns = [
    
    path('clients/', ClientView.as_view(), name='clients'),
    path('client/register/', ClientRegister.as_view(), name='client_register'),

]
