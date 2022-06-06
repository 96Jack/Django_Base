
from One_to_many import views
from django.urls import  path


urlpatterns = [
    path('one/', views.one),
    path('get_dept/', views.get_dept),
    path('get_emp/',views.get_emp),
    path('getDname/', views.getDname),
    path('getEname/',views.getEname),

]

