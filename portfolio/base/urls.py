from django.contrib import admin
from django.urls import path
from. import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('services',views.services, name='services'),
    path('portfolio',views.portfolio, name='portfolio'),
    path('skill',views.skill, name='skill'),
    path('success',views.success_page, name='success'),
    path('contact',views.contact, name='contact')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)