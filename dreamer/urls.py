from django.urls import include, path
from dreamer import views

urlpatterns = [
   path('aprtment/', views.apprtment, name='apartment'),
   path('about/', views.about, name='about'),
   path('review/', views.review, name='review'),
   path('storage/', views.storage, name='storage'),
   path('contact', views.contact, name='contact'),
   path('quote/', views.quote, name='quote'),
   path('office-movi/', views.office_movi, name='office_movi'),
   path('packing/', views.packing, name='packing'),
   path('services', views.services, name='services'),
]