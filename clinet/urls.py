from django.urls import path
from clinet import views


app_name="main"

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.dashboard_login, name="login"),
    path('logout/', views.dashboard_logout, name="logout"),

    path('product_list/', views.product_list, name="product_list"),
    path('product_create/', views.product_create, name="product_create"),
    path('<int:pk>product_edit/', views.product_edit, name="product_edit"),
    path('<int:pk>/product_delete/', views.product_delete, name="product_delete"),

    path('new_list/', views.new_list, name="new_list"),
    path('new_create/', views.new_create, name="new_create"),
    path('<int:pk>new_edit/', views.new_edit, name="new_edit"),
    path('<int:pk>/new_delete/', views.new_delete, name="new_delete"),

    path('gallery_list/', views.gallery_list, name="gallery_list"),
    path('gallery_create/', views.gallery_create, name="gallery_create"),
    path('<int:pk>gallery_edit/', views.gallery_edit, name="gallery_edit"),
    path('<int:pk>/gallery_delete/', views.gallery_delete, name="gallery_delete"),

    path('gallery_list/', views.gallery_list, name="gallery_list"),
    path('gallery_create/', views.gallery_create, name="gallery_create"),
    path('<int:pk>gallery_edit/', views.gallery_edit, name="gallery_edit"),
    path('<int:pk>/gallery_delete/', views.gallery_delete, name="gallery_delete"),

    path('send_list/', views.send_list, name="send_list"),
    path('send_create/', views.send_create, name="send_create"),
    path('<int:pk>/send_edit/', views.send_edit, name="send_edit"),
    path('<int:pk>/send_delete/', views.send_delete, name="send_delete"),

    path('pdf_list/', views.pdf_list, name="pdf_list"),
    path('pdf_create/', views.pdf_create, name="pdf_create"),
    path('<int:pk>/pdf_edit/', views.pdf_edit, name="pdf_edit"),
    path('<int:pk>/pdf_delete/', views.pdf_delete, name="pdf_delete"),


]