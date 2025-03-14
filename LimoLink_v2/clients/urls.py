from django.urls import path
from .views import client_delete, client_list, client_detail, client_create, client_update, ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView

app_name = "clients" 

urlpatterns = [
    path('', ClientListView.as_view(), name="client-list"),  
    path('create/', ClientCreateView.as_view(), name="client-create"),
    path('<int:pk>/delete/', ClientDeleteView.as_view(), name="client-delete"),
    path('<int:pk>/', ClientDetailView.as_view(), name="client-detail"), 
    path('<int:pk>/update/', ClientUpdateView.as_view(), name="client-update"), 
]

