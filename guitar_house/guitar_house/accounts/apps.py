from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'guitar_house.accounts'


    def ready(self):
        import guitar_house.accounts.signals
