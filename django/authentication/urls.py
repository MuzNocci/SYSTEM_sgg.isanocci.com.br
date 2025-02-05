from django.urls import path
from authentication.views import LoginView, LogoutView



urlpatterns = [
    
    path('', LoginView.as_view(), name='login_view'),
    path('auth/logout/', LogoutView.as_view(), name='logout_view'),

]