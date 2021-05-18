from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/add', views.add_form),
    path('shows/edit/<int:val>', views.edit_form),
    path('shows/details/<int:val>', views.details),
    path('deleting/<int:val>', views.delete),
    path('adding', views.adding),
    path('editing/<int:val>', views.editing)
]