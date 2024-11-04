from django.contrib import admin
from django.urls import include, path
from clients.views import landing_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing-page'),
    path('clients/', include('clients.urls', namespace="clients")),
]
