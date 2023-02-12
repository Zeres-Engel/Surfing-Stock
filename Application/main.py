#Import uis
from gui.core.functions import Functions
from gui.uis.windows.main_window.functions_main_window import *
import sys
import os
#Import libraries
from qt_core import *
#Import
from gui.core.json_settings import Settings
from gui.uis.windows.main_window import *
from gui.widgets import *
os.environ["QT_FONT_DPI"] = "96"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #Main UI
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
        #Settings
        settings = Settings()
        self.settings = settings.items
        #Setup main window
        self.hide_grips = True # Show/Hide resize grips
        SetupMainWindow.setup_gui(self)
        #Show
        self.show()

    #Left Button
    def btn_clicked(self):
        #Get cliked
        btn = SetupMainWindow.setup_btns(self)
        if btn.objectName() != "btn_settings":
            self.ui.left_menu.deselect_all_tab()
        
        #* Home button
        if btn.objectName() == "btn_home":
            self.ui.left_menu.select_only_one(btn.objectName())
            #Load page
            MainFunctions.set_page(self, self.ui.load_pages.page_1)

        #* Show Custom Widgets
        if btn.objectName() == "btn_widgets":
            self.ui.left_menu.select_only_one(btn.objectName())
            #Load Page 2
            MainFunctions.set_page(self, self.ui.load_pages.page_2)

        #* Add User
        if btn.objectName() == "btn_add_user":
            self.ui.left_menu.select_only_one(btn.objectName())
            #Load Page 3 
            MainFunctions.set_page(self, self.ui.load_pages.page_3)

        #* Information
        if btn.objectName() == "btn_info":
            #Check information
            if not MainFunctions.left_column_is_visible(self):
                self.ui.left_menu.select_only_one_tab(btn.objectName())
                #Show / Hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    #Show / Hide
                    MainFunctions.toggle_left_column(self)
                
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            #Change Left Column Menu
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self, 
                    menu = self.ui.left_column.menus.menu_2,
                    title = "Info tab",
                    icon_path = Functions.set_svg_icon("icon_info.svg")
                )

        #* Setting
        if btn.objectName() == "btn_settings" or btn.objectName() == "btn_close_left_column":
            #Check setting
            if not MainFunctions.left_column_is_visible(self):
                # Show / Hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    # Show / Hide
                    MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            #Close Infomation
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self, 
                    menu = self.ui.left_column.menus.menu_1,
                    title = "Settings Left Column",
                    icon_path = Functions.set_svg_icon("icon_settings.svg")
                )
        print(f"Button {btn.objectName()}, clicked!")

    #Debuger Button
    def btn_released(self):
        btn = SetupMainWindow.setup_btns(self)
        print(f"Button {btn.objectName()}, released!")

    #Resize event
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    #Mouse press event
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

if __name__ == "__main__":
    #Application
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    #Execute application
    sys.exit(app.exec_())