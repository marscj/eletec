from rest_framework import  serializers

from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import UploadImage

class UploadImageSerializer(serializers.ModelSerializer):

    image = VersatileImageFieldSerializer(required=False, allow_null=True, sizes='image_size')
    
    object_id = serializers.IntegerField()
    
    class Meta:
        model = UploadImage
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):

    image = VersatileImageFieldSerializer(required=False, allow_null=True, sizes='image_size')

    