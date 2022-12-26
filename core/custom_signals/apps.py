from django.apps import AppConfig


class CustomSignalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_signals'

    # def ready(self):
    #     import custom_signals.signals