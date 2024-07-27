from django.urls import path
from . import views



urlpatterns = [
    path('', views.community, name='posts'),
    path('<slug:slug>', views.post_page, name='posts'),
]
