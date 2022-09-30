import time
# QT
from PyQt5 import QtCore
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from utils_huy_quang.detect_yolov5 import Tracking
from queue import Queue


class ProcessLPThread(QtCore.QThread):
    def __init__(self, queue_capture, queue_tracking, queue_show):
        super().__init__()
        # id
        self.__thread_active = False
        self.tracking = Tracking()

        # queues
        self.queue_capture = queue_capture
        self.queue_tracking = queue_tracking
        self.queue_show = queue_show

    def run(self):
        weight_path = r"weights/yolov5s.pt"
        classes = [2, 7]
        conf = 0.7
        imgsz = 640
        device = "cpu"
        self.tracking.setup_model(weight_path, classes, conf, imgsz, device)
        self.__thread_active = True
        print('Starting Process LP...')
        while self.__thread_active:
            if not self.queue_capture.qsize() >= 1:
                time.sleep(0.001)
                continue
            frame = self.queue_capture.get()
            id_dict = self.tracking.detect(frame)
            for id in id_dict.keys():
                x1, y1, x2, y2, category = id_dict[id]
            #   cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            #   cv2.putText(frame, str(id), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            id_dict['image'] = frame
            if self.queue_tracking.qsize() < 1:
                self.queue_tracking.put(id_dict)
            if self.queue_show.qsize() < 1:
                self.queue_show.put(id_dict)

            QtCore.QThread.msleep(1)

    def stop(self):
        print('Stopping Processing Thread')

        self.__thread_active = False


if __name__ == '__main__':
    queue_1 = Queue()
    queue_2 = Queue()
    process = ProcessLPThread(queue_1, queue_2)
    process.start()
