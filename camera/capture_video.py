import cv2
import sys
sys.path.append('../')
from main.models import Records, Settings
from threading import Thread
import os

class Live_Stream():
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes(), image

def gen(camera):
    recording_boolean = Settings.objects.get(pk = 1).recording
    file = open('recording_switch.txt', 'r')
    file_data = file.read()
    file.close()
    if Settings.objects.get(pk = 1).recording == True or file_data == "True-Current":
        recording_boolean = True
        record_last = Records.objects.last()
        date = record_last.datetime.strftime('%Y-%m-%d')
        id = str(record_last.id)
        record_last.relative_path = '/' + date + '/' + id + '.mp4'
        record_last.save()
        path = Settings.objects.get(pk = 1).path
        print('********', date, id , path , Records.objects.last().relative_path)
        if os.path.exists(path + '/' + date) == True:
            pass
        else:
            os.mkdir(path + '/' + date)

        fourcc = cv2.VideoWriter_fourcc(*'H264')
        out = cv2.VideoWriter(path + Records.objects.last().relative_path,
                              fourcc,
                              Settings.objects.get(pk=1).fps,
                              (640, 480))
        print('video part covered........')
        if file_data == 'True-Current':
            file = open('recording_switch.txt', 'w')
            file.write('False')
            file.close()
    if recording_boolean == True:
        while True:
            frame, image = camera.get_frame()
            # image is for recording and frame is for live streaming
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

            out.write(image)
            # recording video
    else:
        while True:
            frame, image = camera.get_frame()
            # image is for recording and frame is for live streaming
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

if __name__ == '__main__':
    pass