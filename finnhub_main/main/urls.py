
from django.urls import path, include

from . import views

urlpatterns = [
    path('companies', views.CompanyList.as_view(), name='companies')
]