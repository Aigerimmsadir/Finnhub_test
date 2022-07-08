from rest_framework import viewsets, status
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Company
from .serializers import *
import datetime
from rest_framework import mixins
from rest_framework import generics


# Create your views here.


class CompanyList(mixins.ListModelMixin,
                  generics.GenericAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get(self, request, *args, **kwargs):
        self.queryset = Company.objects.all()
        date_from = self.kwargs.get('date_from')
        date_to = self.kwargs.get('date_to')
        print(date_from, self.kwargs)
        if date_from:
            date_from = datetime.datetime.strptime(date_from, "%Y-%m-%d").replace(hour=0, minute=0)
            self.queryset = self.queryset.filter(datetime_created__lte=date_from)
        if date_to:
            date_to = datetime.datetime.strptime(date_from, "%Y-%m-%d").replace(hour=23, minute=59, second=59)
            self.queryset = self.queryset.filter(datetime_created__gte=date_to)
        return self.list(request, *args, **kwargs)
