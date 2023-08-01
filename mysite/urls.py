from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('polss/', include('polss.urls')),
    path('admin/', admin.site.urls),
    
]
