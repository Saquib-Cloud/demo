from django.urls import path
from .import views


urlpatterns = [
    path("", views.home, name='home'),
    path('firm/', views.firm,name='firm'),
    path('contact/', views.contact,name='contact'),

]