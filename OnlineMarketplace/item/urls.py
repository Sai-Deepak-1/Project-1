from django.urls import path

from . import views

app_name = 'item'

urlpatterns = [
    path("item/<int:pk>/", views.details, name = 'details' ),
]
