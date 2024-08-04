from django.urls import path
from . import views



urlpatterns = [
    path('', views.community, name='posts'),
    path('post/<slug:slug>/', views.post_page, name='post_page'),
    
]
