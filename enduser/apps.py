from django.apps import AppConfig


class EnduserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'enduser'

    def ready(self) -> None:
        import enduser.signals
