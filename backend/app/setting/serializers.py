from rest_framework import serializers

from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import Faq, App

class FaqSerializer(serializers.ModelSerializer):

    class Meta:
        model = Faq
        fields = '__all__'

class AppSerializer(serializers.ModelSerializer):

    image = VersatileImageFieldSerializer(sizes='app')

    class Meta:
        model = App
        fields = '__all__'

        
