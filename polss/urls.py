from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('eae',views.eae,name='eae'),
    path('opa/',views.opa, name='opa')
    
    ]