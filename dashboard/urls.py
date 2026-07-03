from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_index_page, name='dashboard'),
]