from rest_framework import serializers
from .models import Oxygen_Leads

class Oxy_Serializer(serializers.ModelSerializer):
    class Meta:
          model = Oxygen_Leads
          fields = '__all__'
