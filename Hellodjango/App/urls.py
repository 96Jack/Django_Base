from django.urls import path ,re_path
from App import views


urlpatterns = [
    path('index_app/', views.index_app),
    re_path(r'^a/', views.app_html),
    path('pro_h/', views.pro_html),
    path('one/', views.one),
    path('two/', views.two),
    path('three/', views.three),
    path('add_user/', views.add_User),
    path('findByid/', views.findByid),
    path('findAll/', views.findAll),
    path('update/', views.update),
    path('delete/', views.delete),
    path('get_grade/', views.get_grade),
    path('get_student/', views.get_student)
]