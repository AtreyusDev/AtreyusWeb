from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)