import random
import time
# QT
from PyQt5 import QtCore
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from PyQt5.QtCore import pyqtSignal
import cv2
from utils_huy_quang.detect_yolov5 import Tracking


class ProcessD3Thread(QtCore.QThread):
    def __init__(self, queue_capture, queue_tracking):
        super().__init__()
        # id
        self.__thread_active = False
        self.tracking = Tracking()

        # queues
        self.queue_D3 = queue_capture
        self.queue_tracking = queue_tracking

    def run(self):
        weight_path = r"weights/yolov5m.pt"
        classes = [2, 7]
        conf = 0.4
        imgsz = 640
        device = "0"
        self.tracking.setup_model(weight_path, classes, conf, imgsz, device)
        self.__thread_active = True
        print('Starting Process D3...')
        while self.__thread_active:
            if not self.queue_D3.qsize() >= 1:
                time.sleep(0.001)
                continue
            frame = self.queue_D3.get()
            id_dict = self.tracking.detect(frame)
            if self.queue_tracking.qsize() < 1:
                id_dict['image'] = frame
                self.queue_tracking.put(id_dict)
            QtCore.QThread.msleep(1)

    def stop(self):
        print('Stopping Processing Thread')

        self.__thread_active = False
