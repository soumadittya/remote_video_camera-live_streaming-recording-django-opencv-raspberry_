import sys
sys.path.append('../')
from django.http import HttpResponse, HttpResponseServerError
from django.http.response import StreamingHttpResponse
from camera.capture_video import Live_Stream, gen
from django.shortcuts import redirect, render
from django.views.decorators import gzip
from django.contrib import messages
from .models import Records, Settings
from .forms import Settings_Form
from django.contrib.auth.decorators import login_required
import datetime
import os

@login_required
def index(request):
    if request.method == 'POST':
        pass
    else:
        settings = Settings.objects.get(pk = 1)
        file = open('recording_switch.txt', 'r')
        file_data = file.read()
        file.close()
        if file_data == 'True-Current':
            file_data = True
        else:
            file_data = False
        return render(request, 'index.html',
                      {'settings' : settings,
                        'recording_current' : file_data})

def watch_video(request, log_id = ""):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'watch_video.html',
                      {'watch_video_path' : Settings.objects.get(pk = 1).path + Records.objects.get(pk = log_id).relative_path})

def logs(request):
    if request.method == "POST":
        print('logs post block reached....')
        logs_filter = Records.objects.filter(
            datetime__range = [request.POST.get('date_range_start'),
                               request.POST.get('date_range_stop')]
        )
        print('date filtering done....')
        print(logs_filter)
        path = Settings.objects.get(pk=1).path
        return render(request, 'logs.html', {'logs': logs_filter,
                                             'path': path})
    else:
        logs = Records.objects.all()
        path = Settings.objects.get(pk = 1).path
        return render(request, 'logs.html', {'logs' : logs,
                                             'path' : path})

def delete_log_confirm(request, log_id):
    if request.method == 'POST':
        return redirect('main:delete_log', log_id)
    else:
        return render(request, 'delete_log_confirm.html',
                      {'log_id' : log_id})

def delete_log(request, log_id):
    record = Records.objects.get(id = log_id)
    path = Settings.objects.get(pk = 1).path + record.relative_path
    if os.path.exists(str(path)):
        os.remove(str(path))
    else:
        pass
    record.delete()
    messages.success(request, 'Successfully deleted the selected log....')
    return redirect('main:logs')

def settings(request):
    if request.method == "POST":
        print('POST request accepted....')
        form = Settings_Form(request.POST)
        print('form loaded....')
        if form.is_valid():
            new = Settings.objects.get(pk=1)
            if form.cleaned_data.get('path') == 'static/media' or form.cleaned_data.get('path') == 'static/media/':
                new.path = 'static/media'
            else:
                new.path = 'static/media' + form.cleaned_data.get('path')
            new.recording = form.cleaned_data.get('recording')
            new.fps = form.cleaned_data.get('fps')
            new.save()
        return redirect('main:settings_save')
    else:
        existing_data = Settings.objects.get(pk = 1)
        return render(request, 'settings.html',
                      {'form' : Settings_Form})
def settings_save(request):
    return render(request, 'settings_save.html', {})

@gzip.gzip_page
def video_stream(request):
    print('index block reached....')
    file = open('recording_switch.txt', 'r')
    file_data = file.read()
    file.close()
    print('**** file_data = ', file_data)
    if file_data == 'True-Current':
        obj = Records.objects.last()
        obj.continued = True
        obj.save()
    elif Settings.objects.get(pk=1).recording == True:
        obj = Records.objects.create(user=request.user,
                                     recording=True,
                                     datetime=datetime.datetime.now())
        obj.save()
    else:
        print('else block entered....')

        obj = Records.objects.create(user=request.user,
                                     datetime=datetime.datetime.now())
        print('object created successfully....')
        obj.save()
        print('object saved successfully....')
    print('just before return....')
    try:
        return StreamingHttpResponse(gen(Live_Stream()),content_type="multipart/x-mixed-replace;boundary=frame")
    except HttpResponseServerError as e:
        print("aborted")

@login_required()
def video_record_current(request):
    file = open('recording_switch.txt', 'w')
    file.write('True-Current')
    file.close()
    return redirect('main:index')
