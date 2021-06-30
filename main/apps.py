from django.apps import AppConfig
import os

class MainConfig(AppConfig):
    name = 'main'
    # ready function automatically executes when the server starts
    def ready(self):
        print('server started....')
        from .models import Settings
        if Settings.objects.filter(id = 1).exists():
            print('settings already created....')
        else:
            print('settings not found......')
            Settings.objects.create(id = 1,
                                    path = 'static/media/',
                                    recording = True,
                                    fps = 20)
            print('new settings created........')

        settings_obj = Settings.objects.get(pk = 1)
        try:
            if settings_obj.path == "":
                settings_obj.path = 'static/media'
            else:
                if os.path.exists('static/media' + settings_obj.path) == True:
                    pass
                else:
                    os.mkdir('static/media' + settings_obj.path)
        except:
            pass

