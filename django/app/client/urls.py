from django.urls import path
from app.client.views import ClientView



urlpatterns = [
    
    path('clients/', ClientView.as_view(), name='clients'),

]
