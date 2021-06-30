from django.urls import path
from . import views
from .models import Settings

urlpatterns = [
    path('', views.index, name = 'index'),
    path('index/', views.index, name = 'index'),
    path('video/', views.video_stream, name = 'video'),
    path('record/', views.video_record_current, name = 'record'),
    path('logs/', views.logs, name = 'logs'),
    path('delete_log/<log_id>/', views.delete_log, name = "delete_log"),
    path('delete_log_confirm/<log_id>', views.delete_log_confirm, name = 'delete_log_confirm'),
    path('settings/', views.settings, name = 'settings'),
    path('settings_save/', views.settings_save, name = 'settings_save'),
    path('watch_video/<log_id>/', views.watch_video, name = 'watch_video'),
]