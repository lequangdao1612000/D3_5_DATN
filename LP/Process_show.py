# QT
from PyQt5 import QtCore
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import cv2
from utils_huy_quang.detect_yolov5 import Detection
from LP.Polygon import detect_zone
from Database.utils import Database


class ProcessShowThread(QtCore.QThread, Detection):
    def __init__(self, queue_show, queue_digit, queue_output):
        super().__init__()
        # id
        self.__thread_active = True
        self.crop_size = 300
        # queues
        self.queue_show = queue_show
        self.queue_digit = queue_digit
        self.queue_output = queue_output

        self.database = Database()
        self.count_car = self.database.get_number_of_rows()
        self.old_count_car = 0

    def run(self):
        lp = ""
        color = ""
        brand = ""
        crop_list = []
        last_crop = None
        last_id = 0
        while self.__thread_active:
            if self.queue_show.qsize() < 1:
                QtCore.QThread.msleep(1)
                continue
            id_dict = self.queue_show.get()
            image = id_dict['image']
            image_copy = image.copy()
            H, W = image.shape[:2]
            cv2.fillPoly(image, [detect_zone], (0, 127, 0))
            if self.queue_digit.qsize() > 0:
                digit_dict = self.queue_digit.get()
                lp = digit_dict['lp']
                color = digit_dict['color']
                brand = digit_dict['brand']
            for id in id_dict.keys():
                if id == 'image':
                    continue
                x1, y1, x2, y2, category = id_dict[id]
                is_in_detect_zone = cv2.pointPolygonTest(detect_zone, (x1 // 2, y2), False)
                if is_in_detect_zone < 1:
                    if y2 < H - 300:
                        continue
                    if id != last_id and crop_list:
                        self.count_car += 1
                        last_crop = crop_list[int(len(crop_list) / 2)]
                        last_crop = cv2.resize(last_crop, (self.crop_size, self.crop_size))
                        cv2.imwrite(f"ImageStorage/{self.count_car}.jpg", last_crop)
                        last_id = id
                        crop_list = []
                    continue
                crop = image_copy[y1:y2, x1:x2]
                crop_list.append(crop)
                cv2.fillPoly(image, [detect_zone], (0, 255, 0))
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(image, str(id), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.rectangle(image, (0, 0), (self.crop_size, 200 + self.crop_size), (0, 0, 0), -1)
            image = cv2.addWeighted(image, 0.5, image_copy, 0.5, 0)
            if lp or color or brand:
                cv2.putText(image, f"LP: {lp}", (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                #cv2.putText(image, f"Color: {color}", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                #cv2.putText(image, f"Brand: {brand}", (0, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                if last_crop is not None:
                    if self.old_count_car != self.count_car:
                        dictionary = {"id": self.count_car, "plate": lp, "color": color, "brand": brand,
                                      "img_path": f"ImageStorage/{self.count_car}.jpg"}
                        print(dictionary)
                        self.database.insert_to_db(dictionary)
                        self.old_count_car = self.count_car
                    image[200:200 + self.crop_size, 0:self.crop_size] = last_crop

            if self.queue_output.qsize() < 1:
                self.queue_output.put(image)
            QtCore.QThread.msleep(1)

    def stop(self):
        print('Stopping Processing Thread')

        self.__thread_active = False
