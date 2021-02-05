from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView


favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('API.api_urls')),
    path('favicon.ico/', favicon_view),
]
