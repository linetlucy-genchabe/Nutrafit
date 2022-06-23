from django.apps import AppConfig


class NutrafitConfig(AppConfig):
    name = 'nutrafit'

    def ready(self):
        import nutrafit.signals 
