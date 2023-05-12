from django.urls import path,include
from . import views #IMORTING VIEWS 
from django.conf import settings # IMPORTING SETTINGS
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('rooms/<str:pk>/', views.rooms, name='rooms'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('gallery', views.gallery, name='gallery'),
    path('property', views.property, name='property'),
]+ static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
