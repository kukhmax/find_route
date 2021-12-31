from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:pk>/', views.CityDetailView.as_view(), name='detail'),
]
