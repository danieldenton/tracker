from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('<int:id>/', views.edit, name='edit'),
    path('<int:id>/delete/', views.delete, name='delete')
]