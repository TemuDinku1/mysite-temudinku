from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
     path('<int:product_id>/comment/',
         views.product_comment, name='product_comment'),
     
     #No model is needed for these urls
     path('services/', views.product_services, name='product_services'),
     path('about/', views.product_about, name='product_about'),
     path('contact/', views.product_contact, name='product_contact'),

     #main views
     path('', views.product_list, name='product_list'),
     path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
     path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),

]
