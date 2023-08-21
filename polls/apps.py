from django.apps import AppConfig

#what to add to settings.py installed_apps
class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
