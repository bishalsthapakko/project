from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('instruments/', views.instruments, name='instruments'),
    path('checkout/', views.checkout, name='checkout'),
    
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urls.py (app level)