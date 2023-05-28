from django.urls import path
from . import views

app_name='face'
urlpatterns = [
    
    path('', views.home, name='home'),
    path('my_view/', views.my_view, name='my_view'),
    path('project_view/<int:pv>', views.detail_view, name='project_view'),
    path('delete/<int:dlid>/',views.delete,name='delete'),


]