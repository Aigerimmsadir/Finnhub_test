from rest_framework import serializers
from .models import *


class CompanyNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyNew
        fields = '__all__'