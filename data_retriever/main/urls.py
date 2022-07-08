from django.urls import path, include

from . import views

urlpatterns = [
    path('rr', views.current_datetime)
]
