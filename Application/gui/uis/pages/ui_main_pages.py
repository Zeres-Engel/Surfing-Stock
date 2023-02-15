from PySide6.QtCore import QSize, QMetaObject, QCoreApplication
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QVBoxLayout, QStackedWidget, QWidget, QFrame, QLabel

class Ui_MainPages(object): 
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(860, 600)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 14pt")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.welcome_base = QFrame(self.page_1)
        self.welcome_base.setObjectName(u"welcome_base")
        self.welcome_base.setMinimumSize(QSize(300, 150))
        self.welcome_base.setMaximumSize(QSize(300, 150))
        self.welcome_base.setFrameShape(QFrame.NoFrame)
        self.welcome_base.setFrameShadow(QFrame.Raised)
        self.center_page_layout = QVBoxLayout(self.welcome_base)
        self.center_page_layout.setSpacing(10)
        self.center_page_layout.setObjectName(u"center_page_layout")
        self.center_page_layout.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.welcome_base)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(300, 120))
        self.logo.setMaximumSize(QSize(300, 120))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)
        self.logo_layout = QVBoxLayout(self.logo)
        self.logo_layout.setSpacing(0)
        self.logo_layout.setObjectName(u"logo_layout")
        self.logo_layout.setContentsMargins(0, 0, 0, 0)
        self.center_page_layout.addWidget(self.logo)
        self.label = QLabel(self.welcome_base)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)
        self.center_page_layout.addWidget(self.label)
        
        
        #Page 1
        self.chart_progress_1_layout = QVBoxLayout()
        self.chart_progress_1_layout.setObjectName(u"chart_progress_1_layout")
        self.page_1_layout.addLayout(self.chart_progress_1_layout)
        self.pages.addWidget(self.page_1)
        
        #Page 2
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"font-size: 14pt")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.chart_progress_2_layout = QVBoxLayout()
        self.chart_progress_2_layout.setObjectName(u"chart_progress_2_layout")
        self.page_2_layout.addLayout(self.chart_progress_2_layout)
        self.pages.addWidget(self.page_2)
        
        #Page 3
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"font-size: 14pt")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setSpacing(5)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.page_3_layout.setContentsMargins(5, 5, 5, 5)
        self.chart_progress_3_layout = QVBoxLayout()
        self.chart_progress_3_layout.setObjectName(u"chart_progress_3_layout")
        self.page_3_layout.addLayout(self.chart_progress_3_layout)
        self.pages.addWidget(self.page_3)
        
        #Main Page
        self.main_pages_layout.addWidget(self.pages)
        self.retranslateUi(MainPages)
        self.pages.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainPages)

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
