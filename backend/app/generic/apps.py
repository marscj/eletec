from django.apps import AppConfig


class GenericConfig(AppConfig):
    name = 'app.generic'

    # def ready(self):
    #     from .import handle