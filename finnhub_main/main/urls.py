
from django.urls import path, include

from . import views

urlpatterns = [
    path('companynews', views.CompanyNewList.as_view(), name='companynews')
]