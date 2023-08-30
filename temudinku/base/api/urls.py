from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('v2/', views.getProduct),
]
