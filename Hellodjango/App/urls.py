from django.urls import path ,re_path
from App import views

urlpatterns = [
    path('index_app/', views.index_app),
    re_path(r'^a/', views.app_html),
    path('pro_h/', views.pro_html),

]