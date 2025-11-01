# properties/apps.py
from django.apps import AppConfig

class PropertiesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'properties'
    label = 'properties' # Keep the explicit label fix

    def ready(self):
        # IMPORTANT: Import signals here to register the handlers
        import properties.signals
