import time
# QT
from PyQt5 import QtCore
import os
import cv2
import numpy as np
from color_brand.classify import Classifier
from utils_huy_quang.detect_yolov5 import Detection
from LP.utils import check

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"


class ProcessDigitThread(QtCore.QThread):
    sig_car_info = QtCore.pyqtSignal(dict)

    def __init__(self, queue_lp_process, queue_digit):
        super().__init__()

        self.weight_path = r"C:\Users\ASUS\Desktop\daoquang1612\parking_project\datn\YOLO_v4_file\lp.weights"
        self.cfg_path = r"C:\Users\ASUS\Desktop\daoquang1612\parking_project\datn\YOLO_v4_file\base_data_tiny.cfg"
        self.class_path = r"C:\Users\ASUS\Desktop\daoquang1612\parking_project\datn\YOLO_v4_file\obj.names"
        self.net = cv2.dnn.readNet(self.weight_path, self.cfg_path)
        self.classes = self.get_classes()
        self.scale = 1 / 255.
        self.size = (224, 224)
        self.conf_threshold = 0.3
        self.nms_threshold = 0.4
        #self.classifier_color = Classifier("color_brand/color.mnn", "color_brand/labels-color.txt")
        self.detection = Detection()

        # queue
        self.queue_lp_process = queue_lp_process
        self.queue_digit = queue_digit

    def get_classes(self):
        with open(self.class_path, 'r') as f:
            self.classes = [line.strip() for line in f.readlines()]
        return self.classes

    def get_output_layers(self, net):
        layer_names = net.getLayerNames()

        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

        return output_layers

    def is_square_lp(self, image):
        return image.shape[1] / image.shape[0] <= 2

    def process_square_lp(self, bboxes):
        line_1 = []
        line_2 = []
        all_y = [box[1] for box in bboxes]
        if len(all_y) == 0:
            return []
        average_y = sum(all_y) / len(all_y)
        for bbox in bboxes:
            if bbox[1] < average_y:
                line_1.append(bbox)
            else:
                line_2.append(bbox)
        line_1 = sorted(line_1, key=lambda x: x[0])
        line_2 = sorted(line_2, key=lambda x: x[0])
        return line_1 + line_2

    def run(self):
        self.__thread_active = True
        weight_path = r"weights/brand.pt"
        classes = None
        conf = 0.2
        imgsz = 640
        device = "0"
        self.detection.setup_model(weight_path, classes, conf, imgsz, device)
        print('Starting Digits Thread...')
        count = 0
        lp_list = []
        color_list = []
        brand_list = []
        count_missing_lp = 0
        while self.__thread_active:
            if self.queue_lp_process.qsize() < 1:
                count_missing_lp += 1
                if count_missing_lp > 30:
                    count_missing_lp = 0
                    lp_final = check(lp_list)
                    color_final = check(color_list)
                    brand_final = check(brand_list)
                    if brand_final:
                        brand_final = brand_final.split("____")[1]
                    if lp_final or brand_final or color_final:
                        return_dict = {'lp': lp_final, 'color': color_final, 'brand': brand_final}
                        if self.queue_digit.qsize() < 1:
                            self.queue_digit.put(return_dict)
                        self.sig_car_info.emit(return_dict)
                    lp_list = []
                    brand_list = []
                    color_list = []
                time.sleep(0.001)
                continue
            lp_dict = self.queue_lp_process.get()
            img = lp_dict['image']
            count += 1
            for key in lp_dict.keys():
                if key == 'image':
                    continue
                x1, y1, x2, y2, x1_crop, y1_crop, x2_crop, y2_crop = lp_dict[key]
                car_crop = img[y1:y2, x1:x2]

                # Color
                color, color_conf = self.classifier_color.predict(car_crop)
                if color_conf > 0.3:
                    color_list.append(color)

                # Brand
                brands_detection = self.detection.detect(car_crop)
                if brands_detection:
                    _, _, _, _, brand = brands_detection[0]
                    brand_list.append(brand)

                image = car_crop[y1_crop:y2_crop, x1_crop:x2_crop]
                Width = image.shape[1]
                Height = image.shape[0]
                blob = cv2.dnn.blobFromImage(image, self.scale, self.size, (0, 0, 0), True, crop=False)

                self.net.setInput(blob)

                outs = self.net.forward(self.get_output_layers(self.net))

                class_ids = []
                confidences = []
                boxes = []

                for out in outs:
                    for detection in out:
                        scores = detection[5:]
                        class_id = np.argmax(scores)
                        confidence = scores[class_id]
                        if confidence > self.conf_threshold:
                            center_x = int(detection[0] * Width)
                            center_y = int(detection[1] * Height)
                            w = int(detection[2] * Width)
                            h = int(detection[3] * Height)
                            x = center_x - w / 2
                            y = center_y - h / 2
                            class_ids.append(class_id)
                            confidences.append(float(confidence))
                            boxes.append([x, y, w, h])

                indices = cv2.dnn.NMSBoxes(boxes, confidences, self.conf_threshold, self.nms_threshold)

                bboxes = []

                for i in indices:
                    i = i[0]
                    box = list(map(int, boxes[i]))
                    x = box[0]
                    y = box[1]
                    w = box[2]
                    h = box[3]
                    bboxes.append([x, y, w, h, confidences[i], class_ids[i]])

                bboxes = sorted(bboxes, key=lambda x: x[0])
                is_square = self.is_square_lp(image)
                if is_square:
                    bboxes = self.process_square_lp(bboxes)
                lp_text = ""
                for bbox in bboxes:
                    x, y, w, h, confidence, class_id = bbox
                    lp_text += self.classes[class_id]
                lp_text = lp_text.upper().strip()
                if (not lp_text) or lp_text[2].isdigit():
                    continue
                lp_list.append(lp_text)
                # cv2.imshow("image", car_crop)
                # cv2.waitKey(1)

    def stop(self):
        print('Stopping Processing Thread')

        self.__thread_active = False
