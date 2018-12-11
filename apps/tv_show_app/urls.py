from django.urls import path
from . import views

app_name="tv_show_app"
urlpatterns = [
    path('shows/', views.index),
    path('shows/new/', views.new),
    path('shows/create', views.create),
    path('shows/<number>/', views.show),
    path('shows/<number>/edit/', views.edit),
    path('shows/<number>/update/', views.update),
    path('shows/<number>/destroy/', views.destroy)
]