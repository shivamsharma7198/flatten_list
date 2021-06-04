from django.urls import path
from . import views

urlpatterns = [
    path('', views.oxy_lead, name = 'oxy_lead'),

]