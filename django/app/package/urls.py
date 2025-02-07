from django.urls import path
from app.package.views import PlansView, PlanRegister, PlanUpdate, PlanDelete
from app.package.views import PackagesView, PackageRegister, PackageUpdate, PackageDelete



urlpatterns = [
    
    path('plans/', PlansView.as_view(), name='plans_view'),
    path('plan/register/', PlanRegister.as_view(), name='plan_register'),
    path('plan/<uuid:id>/update/', PlanUpdate.as_view(), name='plan_update'),
    path('plan/<uuid:id>/delete/', PlanDelete.as_view(), name='plan_delete'),

    path('packages/', PackagesView.as_view(), name='packages_view'),
    path('package/register/', PackageRegister.as_view(), name='package_register'),
    path('package/<uuid:id>/update/', PackageUpdate.as_view(), name='package_update'),
    path('package/<uuid:id>/delete/', PackageDelete.as_view(), name='package_delete'),

]