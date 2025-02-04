from django.apps import AppConfig  # type: ignore


class Example1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'example1'
