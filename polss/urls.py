from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list,name='home'),
    path('eae',views.eae,name='eae'),
    path('opa/',views.opa, name='opa')
    
    ]