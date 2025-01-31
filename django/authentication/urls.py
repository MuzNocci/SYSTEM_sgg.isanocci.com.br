from django.urls import path
from authentication.views import LoginView



urlpatterns = [
    
    path('', LoginView.as_view(), name='login_view'),

]