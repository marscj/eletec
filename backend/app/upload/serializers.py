from rest_framework import  serializers
from django.contrib.contenttypes.models import ContentType

from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import UploadImage, Image

class ContentTypeField(serializers.Field):

    def to_representation(self, obj):
        return obj.model

    def to_internal_value(self, data):
        return ContentType.objects.get(model=data)


class UploadImageSerializer(serializers.ModelSerializer):

    image = VersatileImageFieldSerializer(required=False, allow_null=True, sizes='image_size')
    
    object_id = serializers.IntegerField()
    
    class Meta:
        model = UploadImage
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):

    image = VersatileImageFieldSerializer(required=False, allow_null=True, sizes='image_size')

    content_type = ContentTypeField()
    
    class Meta:
        model = Image
        fields = '__all__'