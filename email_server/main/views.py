from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import permissions
from django.utils import timezone
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)



class SubscribeToTicket(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request):
        print(self.request.user)
        ticket_name = request.data.get('ticket')
        ticket = TicketInterest.objects.get_or_create(name = ticket_name)[0]
        
        ticket.users_subscribed.add(request.user)
        return Response({'status':'ok'})