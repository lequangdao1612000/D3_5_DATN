import cv2
from widget_layout.main_window import Ui_MainWindow
from PyQt5.QtWidgets import QApplication
import sys
from PyQt5.QtCore import pyqtSignal
from widget_layout.map_2d import Ui_map2D
from widget_layout.layout_search_3 import Ui_Layout_Search
from widget_layout.layout_info_car import Ui_Info_Car
from widget_layout.layout_info_table import Ui_Info_Table
from Database.utils import Database
from PyQt5 import QtWidgets
from PyQt5 import QtCore


class MainWindow(Ui_MainWindow):
    sig_view_2d_map = pyqtSignal(bool)
    sig_view_info = pyqtSignal(bool)
    sig_search = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.map_2d = Ui_map2D()
        self.layout_info_table = Ui_Info_Table()
        self.layout_search = Ui_Layout_Search()

        self.btn_view_2d_map.clicked.connect(self.slot_view_2d_map)
        self.btn_info_table.clicked.connect(self.slot_info_table)
        self.btn_search.clicked.connect(self.slot_search)

        self.layout_search.btn_apply.clicked.connect(self.slot_apply)
        self.layout_search.btn_cancel.clicked.connect(self.slot_cancel)

        self.camera_items_dict[3].process_digit.sig_car_info.connect(self.camera_items_dict[2].slot_lp_from_lp)

        self.database = Database()

        self.widget_list = []

        self.show()

    def slot_apply(self):
        for widget in self.widget_list:
            self.layout_search.scrollAreaWidgetContents.layout().removeWidget(widget)
        plate = self.layout_search.txt_plate.text()
        brand = self.layout_search.txt_brand.text()
        color = self.layout_search.txt_color.text()
        result_dict = self.database.get_info({'plate': plate, 'brand': brand, 'color': color})
        if result_dict:
            count = 0
            self.widget_list = []
            for k, result in result_dict.items():
                count += 1
                plate_ = result['plate']
                color_ = result['color']
                brand_ = result['brand']
                in_time = result['in_time']
                out_time = result['out_time']
                img_path_ = result['img_path']

                self.ui_info_car = Ui_Info_Car()
                self.ui_info_car.qlabel_plate.setText(plate_)
                self.ui_info_car.qlabel_color.setText(color_)
                self.ui_info_car.qlabel_brand.setText(brand_)
                self.ui_info_car.qlabel_in_time.setText(in_time)
                self.ui_info_car.qlabel_out_time.setText(out_time)

                img_path = img_path_
                img = cv2.imread(img_path)
                self.show_frame(self.ui_info_car.qlabel_frame, img)
                self.widget_list.append(self.ui_info_car)
                self.layout_search.scrollAreaWidgetContents.layout().addWidget(self.ui_info_car)

                print(plate_, color_, brand_, in_time, out_time, img_path_)
                if count == 1000:
                    break

    def slot_cancel(self):
        self.layout_search.hide()

    def slot_view_2d_map(self):
        self.map_2d.hide()
        self.map_2d.move(100, 200)
        self.map_2d.show()

    def slot_search(self):
        plates = list(set(self.database.get_plate_list()))
        colors = list(set(self.database.get_color_list()))
        brands = list(set(self.database.get_brand_list()))
        print(plates, colors, brands)

        completer_plate = QtWidgets.QCompleter(plates, self)
        completer_plate.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        completer_color = QtWidgets.QCompleter(colors, self)
        completer_color.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        completer_brand = QtWidgets.QCompleter(brands, self)
        completer_brand.setCaseSensitivity(QtCore.Qt.CaseInsensitive)

        self.layout_search.txt_plate.setCompleter(completer_plate)
        self.layout_search.txt_color.setCompleter(completer_color)
        self.layout_search.txt_brand.setCompleter(completer_brand)

        self.layout_search.hide()
        self.layout_search.move(200, 100)
        self.layout_search.show()

    def slot_car_info_from_lp(self, car_info):
        print(car_info)

    def slot_info_table(self):
        self.layout_info_table.hide()
        self.layout_info_table.db_to_df()
        self.layout_info_table.show_table()
        self.layout_info_table.move(500, 0)
        self.layout_info_table.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    sys.exit(app.exec())
