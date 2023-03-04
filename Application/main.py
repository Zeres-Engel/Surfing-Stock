import os
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QTimer
from gui.core.functions import Functions
from gui.core.json_settings import Settings
from gui.uis.windows.main_window import *
from gui.widgets import *
from gui.uis.windows.main_window.functions_main_window import *

os.environ["QT_FONT_DPI"] = "96"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
        settings = Settings()
        self.settings = settings.items
        self.hide_grips = True
        SetupMainWindow.setup_gui(self)
        self.show()
        self.timer = QTimer(self)
        self.timer.setInterval(60000)
        self.timer.timeout.connect(self.real_time_function) 
        self.timer.start()
        
    def real_time_function(self):
        Functions.Crawlagain(self, 'FPT')
        Functions.Crawlagain(self, 'CTG')
        Functions.Crawlagain(self, 'LCG')

    def btn_clicked(self):
        btn = SetupMainWindow.setup_btns(self)
        
        if btn.objectName() == "btn_FPT":
            self.ui.left_menu.select_only_one(btn.objectName())
            MainFunctions.set_page(self, self.ui.load_pages.page_1)
            
        if btn.objectName() == "btn_CTG":
            self.ui.left_menu.select_only_one(btn.objectName())
            MainFunctions.set_page(self, self.ui.load_pages.page_2)
            
        if btn.objectName() == "btn_LCG":
            self.ui.left_menu.select_only_one(btn.objectName())
            MainFunctions.set_page(self, self.ui.load_pages.page_3)

    def btn_released(self):
        btn = SetupMainWindow.setup_btns(self)

    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
