from main.models import *
from rest_framework import serializers
from main.models import MainUser
import datetime
from django.utils import timezone

class MainUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainUser
        fields = ('username', 'email', 'password')
        write_only_fields = ('password',)

    def create(self, validated_data):
        user = MainUser.objects.create_user(**validated_data)
        return user

