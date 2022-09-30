import random
import time
# QT
from PyQt5 import QtCore
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from PyQt5.QtCore import pyqtSignal
import cv2
from utils_huy_quang.detect_yolov5 import Tracking


class ProcessD5Thread(QtCore.QThread):
    def __init__(self, queue_D5, queue_D5_process):
        super().__init__()
        # id
        self.__thread_active = False
        self.tracking = Tracking()

        # queues
        self.queue_D5 = queue_D5
        self.queue_D5_process = queue_D5_process

    def run(self):
        weight_path = r"weights/yolov5m.pt"
        classes = [2, 7]
        conf = 0.3
        imgsz = 640
        device = "cpu"
        self.tracking.setup_model(weight_path, classes, conf, imgsz, device)
        self.__thread_active = True
        print('Starting Process D5...')
        count = 0
        t = time.time()
        fps = 0
        while self.__thread_active:
            if time.time() - t > 1:
                t = time.time()
                fps = count
                count = 0
            if not self.queue_D5.qsize() >= 1:
                time.sleep(0.001)
                continue
            count += 1
            frame = self.queue_D5.get()
            id_dict = self.tracking.detect(frame)
            for id in id_dict.keys():
                x1, y1, x2, y2, category = id_dict[id]
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, str(id), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, str(fps), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            if self.queue_D5_process.qsize() < 1:
                self.queue_D5_process.put(frame)
            QtCore.QThread.msleep(1)

    def stop(self):
        print('Stopping Processing Thread')

        self.__thread_active = False
