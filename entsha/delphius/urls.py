from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.delphius_home),
    path('insert/', views.delphius_form, name='insert'),
    path('list/', views.delphius_list, name='list'),
    path('delete/', views.delphius_delete, name='delete'),
    path('lead_list/', views.lead_list, name='lead_list'),
    path('lead/', views.lead_form, name='lead'),
    path('interest/', views.interest_form, name='interest'),
    path('interest_list/', views.interest_list, name='interest_list'),

    ]
