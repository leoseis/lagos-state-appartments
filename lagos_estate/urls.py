from django.contrib import admin
from django.urls import path

from appartments.views import (
Appartment_list,
Appartment_retrieve, 
Appartment_create,
Appartment_update,
Appartment_delete
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Appartment_list),
    path('appartments/<pk>/', Appartment_retrieve),
    path('appartments/<pk>/edit/', Appartment_update),
    path('appartment/<pk>/delete/', Appartment_delete),
    path('add-appartment/', Appartment_create)
    
]
