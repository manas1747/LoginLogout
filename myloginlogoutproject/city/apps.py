from django.apps import AppConfig


class CityConfig(AppConfig):
    name = 'city'

    def ready(self):  # this is to import signals.py
        print("at ready")
        import city.signals
