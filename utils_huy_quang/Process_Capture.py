from PyQt5 import QtCore
import os
import cv2

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


class ProcessCaptureThread(QtCore.QThread):
    def __init__(self, queue_capture, rtsp_url, camera_id):
        super().__init__()
        # id
        self.camera_id = camera_id
        self.__thread_active = False
        self.cap = cv2.VideoCapture(rtsp_url)
        self.queue_capture = queue_capture

    def run(self):
        self.__thread_active = True
        print('Starting Process Capture...')
        while self.__thread_active:
            ret, frame = self.cap.read()
            if not ret:
                break
            if self.queue_capture.qsize() < 1:
                self.queue_capture.put(frame)
            QtCore.QThread.msleep(20)

    def stop(self):
        print('Stopping Processing Thread')

        self.__thread_active = False
