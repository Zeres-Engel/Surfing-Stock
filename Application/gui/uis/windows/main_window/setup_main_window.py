import sys
import os
import pandas as pd
from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from . functions_main_window import *
from PySide6.QtGui import QIcon, Qt 
from PySide6.QtSvgWidgets import QSvgWidget
from gui.core.json_settings import Settings
from gui.core.json_themes import Themes
from gui.widgets import PyGrips, PyPushButton
from gui.core.functions import Functions
import numpy as np
class SetupMainWindow:
    def __init__(self):
        super().__init__()
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
    add_left_menus = [
        {
            "btn_icon" : "icon_FPT.svg",
            "btn_id" : "btn_FPT",
            "btn_text" : "Công ty Cổ phần FPT",
            "btn_tooltip" : "FPT",
            "show_top" : True,
            "is_active" : True
        },
        {
            "btn_icon" : "icon_CTG.svg",
            "btn_id" : "btn_CTG",
            "btn_text" : "Ngân hàng TMCP Công Thương",
            "btn_tooltip" : "CTG",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_LCG.svg",
            "btn_id" : "btn_LCG",
            "btn_text" : "Công ty Cổ phần LIZEN",
            "btn_tooltip" : "LCG",
            "show_top" : True,
            "is_active" : False
        }
    ]
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()
    def setup_gui(self):
        self.setWindowTitle(self.settings["app_name"])
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Welcome to PyOneDark")
        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)
        MainFunctions.set_page(self, self.ui.load_pages.page_1)
        MainFunctions.set_left_column_menu(
            self,
            menu = self.ui.left_column.menus.menu_1,
            title = "Settings Left Column",
            icon_path = Functions.set_svg_icon("icon_settings.svg")
        )
        settings = Settings()
        self.settings = settings.items
        themes = Themes()
        self.themes = themes.items
        self.left_btn_1 = PyPushButton(
            text="Btn 1",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.left_btn_1.setMaximumHeight(40)
        self.ui.left_column.menus.btn_1_layout.addWidget(self.left_btn_1)
        self.left_btn_2 = PyPushButton(
            text="Btn With Icon",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon = QIcon(Functions.set_svg_icon("icon_settings.svg"))
        self.left_btn_2.setIcon(self.icon)
        self.left_btn_2.setMaximumHeight(40)
        self.ui.left_column.menus.btn_2_layout.addWidget(self.left_btn_2)
        # BTN 3 - Default QPushButton
        self.left_btn_3 = QPushButton("Default QPushButton")
        self.left_btn_3.setMaximumHeight(40)
        self.ui.left_column.menus.btn_3_layout.addWidget(self.left_btn_3)
        Functions.CrawlCompanies()
        
        FPT = pd.read_csv(f"./data/prepaired/FPTpre.csv", encoding = "utf-8")
        Functions.SetLineGraph(self,FPT,'FPT')
        Functions.Evaluation(self,FPT,'FPT')
        
        CTG = pd.read_csv(f"./data/prepaired/CTGpre.csv", encoding = "utf-8")
        Functions.SetLineGraph(self,CTG,'CTG')
        Functions.Evaluation(self,CTG,'CTG')
        
        LCG = pd.read_csv(f"./data/prepaired/LCGpre.csv", encoding = "utf-8")
        Functions.SetLineGraph(self,LCG,'LCG')
        Functions.Evaluation(self,LCG,'LCG')   
        # PAGE 1
        self.chart_progress_1 = QSvgWidget(Functions.set_svg_image("FPT.svg"))
        self.chart_progress_1.setFixedSize(1200, 600)
        self.ui.load_pages.row_1_1layout.addWidget(self.chart_progress_1, Qt.AlignCenter | Qt.AlignCenter)

        self.chart_progress_2 = QSvgWidget(Functions.set_svg_image("FPTeval.svg"))
        self.chart_progress_2.setFixedSize(1200, 600)
        self.ui.load_pages.row_2_1layout.addWidget(self.chart_progress_2, Qt.AlignCenter | Qt.AlignCenter)
        
        # PAGE 2
        self.chart_progress_1 = QSvgWidget(Functions.set_svg_image("CTG.svg"))
        self.chart_progress_1.setFixedSize(1200, 600)
        self.ui.load_pages.row_1_2layout.addWidget(self.chart_progress_1, Qt.AlignCenter | Qt.AlignCenter)
        
        self.chart_progress_2 = QSvgWidget(Functions.set_svg_image("CTGeval.svg"))
        self.chart_progress_2.setFixedSize(1200, 600)
        self.ui.load_pages.row_2_2layout.addWidget(self.chart_progress_2, Qt.AlignCenter | Qt.AlignCenter)
        
        # PAGE 3
        self.chart_progress_1 = QSvgWidget(Functions.set_svg_image("LCG.svg"))
        self.chart_progress_1.setFixedSize(1200, 600)
        self.ui.load_pages.row_1_3layout.addWidget(self.chart_progress_1, Qt.AlignCenter | Qt.AlignCenter)

        self.chart_progress_2 = QSvgWidget(Functions.set_svg_image("LCGeval.svg"))
        self.chart_progress_2.setFixedSize(1200, 600)
        self.ui.load_pages.row_2_3layout.addWidget(self.chart_progress_2, Qt.AlignCenter | Qt.AlignCenter)
        
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)