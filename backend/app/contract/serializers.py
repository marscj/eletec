
from rest_framework import  serializers

from .models import User, Contract

class ContractSerializer(serializers.ModelSerializer):

    user_id = serializers.IntegerField()
    
    class Meta:
        model = Contract
        fields = '__all__'