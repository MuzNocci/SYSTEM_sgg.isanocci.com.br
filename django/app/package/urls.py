from django.urls import path
from app.package.views import PlansView, PlanRegister, PlanUpdate



urlpatterns = [
    
    path('plans/', PlansView.as_view(), name='plans_view'),
    path('plan/register/', PlanRegister.as_view(), name='plan_register'),
    path('plan/<uuid:id>/update/', PlanUpdate.as_view(), name='plan_update'),

]