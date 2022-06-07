from django.urls import path 
from ModelFilter import views


urlpatterns = [
    path('t_filter/', views.t_filter),
    path('t_in/', views.t_in),
    path('t_exclude/', views.t_exclude),
    path('t_fil_ex/', views.t_fil_ex),
    path('create_obj/', views.create_obj),
    path('QSet/', views.QSet),
    path('getOne/', views.getOne),
]