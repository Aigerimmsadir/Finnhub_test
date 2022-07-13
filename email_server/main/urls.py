from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter() 
router.register(r'user', MainUserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),
     path('subscribe/', SubscribeToTicket.as_view()),
     path('sum/', DailySummary.as_view())
]