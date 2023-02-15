import os
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QApplication
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
    def btn_clicked(self):
        btn = SetupMainWindow.setup_btns(self)
        if btn.objectName() != "btn_settings":
            self.ui.left_menu.deselect_all_tab()     
        if btn.objectName() == "btn_home":
            self.ui.left_menu.select_only_one(btn.objectName())
            MainFunctions.set_page(self, self.ui.load_pages.page_1)
        if btn.objectName() == "btn_widgets":
            self.ui.left_menu.select_only_one(btn.objectName())
            MainFunctions.set_page(self, self.ui.load_pages.page_2)
        if btn.objectName() == "btn_add_user":
            self.ui.left_menu.select_only_one(btn.objectName())
            MainFunctions.set_page(self, self.ui.load_pages.page_3)
        print(f"Button {btn.objectName()}, clicked!")
    def btn_released(self):
        btn = SetupMainWindow.setup_btns(self)
        print(f"Button {btn.objectName()}, released!")
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())