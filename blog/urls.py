from django.urls import path
from . import views

urlpatterns = [
    path('', views.retrieve_blogs, name='retrieve_blogs'),

    path('create/', views.create_blog, name='create_blog'),

    path('update/<int:pk>/', views.update_blog, name='update_blog'),

    
]
