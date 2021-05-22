from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path('create', views.createAPI),
    path('delete/<str:type>/<int:id>', views.deleteAPI),
    path('update/<str:type>/<int:id>', views.updateAPI),
    path('get/<str:type>/<int:id>', views.getAPI),
    path('get/<str:type>', views.get_by_type)
]  