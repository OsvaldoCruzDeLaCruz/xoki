"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import static
from django.conf import settings

from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', HomeView.as_view(), name='home'),
    path('xoki/', include('xoki.urls', namespace='xoki')),
    path('reportes/', include('reportes.urls', namespace='reportes')),
    path('publicaciones/', include('publicaciones.urls', namespace='publicaciones')),
    path('visitas/', include('visitas.urls', namespace='visitas')),

]

if settings.DEBUG:
    urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)