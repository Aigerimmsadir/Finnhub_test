
from django.urls import path, include

from . import views

urlpatterns = [
    path('companies', views.CompanyNewList.as_view(), name='companies')
]