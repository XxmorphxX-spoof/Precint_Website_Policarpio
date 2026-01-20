from django.urls import path
from . import views
# police_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
    path('contact/success/', views.contact_success_view, name='contact_success'),
]

urlpatterns = [
    
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('SubmitContact/', views.contact, name='SubmitContact'),
]