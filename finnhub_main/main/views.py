from rest_framework import viewsets, status
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CompanyNew
from .serializers import *
import datetime
from rest_framework import mixins
from rest_framework import generics


# Create your views here.


class CompanyNewList(mixins.ListModelMixin,
                  generics.GenericAPIView):
    queryset = CompanyNew.objects.all()
    serializer_class = CompanyNewSerializer

    def get(self, request, *args, **kwargs):
        self.queryset = CompanyNew.objects.all()
        date_from = self.request.query_params.get('date_from')
        date_to = self.request.query_params.get('date_to')
        print(date_from,self.request.query_params)
        if date_from:

            date_from = datetime.datetime.strptime(date_from, "%Y-%m-%d").replace(hour=0, minute=0)
            print(date_from)
            self.queryset = self.queryset.filter(datetime_created__gte=date_from)
        if date_to:
            date_to = datetime.datetime.strptime(date_to, "%Y-%m-%d").replace(hour=23, minute=59, second=59)
            self.queryset = self.queryset.filter(datetime_created__lte=date_to)
        return self.list(request, *args, **kwargs)
