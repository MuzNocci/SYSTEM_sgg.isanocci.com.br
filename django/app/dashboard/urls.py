from django.urls import path
from app.dashboard.views import DashboardView



urlpatterns = [
    
    path('dashboard/', DashboardView.as_view(), name='dashboard_view'),

]