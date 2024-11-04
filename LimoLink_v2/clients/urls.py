from django.urls import path
from .views import client_delete, client_list, client_detail, client_create, client_update

app_name = "clients" 

urlpatterns = [
    path('', client_list, name="client-list"),  
    path('create/', client_create, name="client-create"),
    path('<int:pk>/delete/', client_delete, name="client-delete"),
    path('<int:pk>/', client_detail, name="client-detail"), 
    path('<int:pk>/update/', client_update, name="client-update"), 
]