from rest_framework.serializers import ModelSerializer
from .models import *

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class AdvocateSerializer(ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = Advocate
        fields = '__all__'
