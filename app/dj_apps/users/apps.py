from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app.dj_apps.users"

    def ready(self):
        import app.dj_apps.users.signals  # noqa: F401
