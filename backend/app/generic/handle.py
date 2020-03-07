# from django.dispatch import receiver
# from django.db.models.signals import post_save, pre_save, pre_delete, post_delete

# from .models import Image

# @receiver(pre_delete, sender=Image)
# def image_model_post_delete(sender, instance, **kwargs):

#     if instance.image is not None: 
#         instance.image.delete()

