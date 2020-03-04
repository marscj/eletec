from django.apps import AppConfig


class UploadConfig(AppConfig):
    name = 'app.upload'

    def ready(self):
        from .import handle