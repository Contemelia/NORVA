from os import mkdir, listdir, path
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from tkinter import Tk, filedialog
import sys

from Configuration import Configuration
from FileHandler import DataHandler





class UserInterface(QMainWindow):
    
    def __init__(self):
        
        super().__init__()
        
        self.setWindowTitle("NOルVA")
        self.Configuration = Configuration('dark', 'purple')
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setFixedSize(self.Configuration.dimension[0], self.Configuration.dimension[1])
        # self.initiateCommonVariables()
        self.initiateInstance()
        
        
        self.setStyleSheet(self.Configuration.stylesheet)
    
    
    
    def initiateInstance(self):
        
        # Sets the background image for the application.
        background_image_pixmap = QPixmap(".\\Images\\dev-wallpaper.png")
        background_image = QLabel(self)
        background_image.setGeometry(0, 0, self.Configuration.dimension[0], self.Configuration.dimension[1])
        background_image.setPixmap(background_image_pixmap)
        
        # Create a duration for the message bar.
        self.message_duration = QTimer()
        self.message_duration.setInterval(2500)
        
        # Creates a Directory 'Data' in the current working directory if it doesn't exist.
        try:
            mkdir('Data')
        except:
            pass
        
        # Creates a base canvas for the application.
        self.base_canvas = QWidget(self)
        self.base_canvas.setObjectName('baseCanvas')
        self.base_canvas.setGeometry(0, 0, self.Configuration.dimension[0], self.Configuration.dimension[1])
        
        # Creates a stacked widget to hold all the primary pages.
        self.primary_stacked_widget = QStackedWidget(self.base_canvas)
        self.primary_stacked_widget.setObjectName('primaryStackedWidget')
        self.primary_stacked_widget.setFixedSize(self.Configuration.dimension[0], self.Configuration.dimension[1] - 70)
        self.primary_stacked_widget.move(0, 70)
        
        # Creates the necessary containers for the application.
        self.createNavigationBar()
        self.createFileList()
    
    
    
    def createNavigationBar(self):
        
        self.navigation_bar_container = QWidget(self.base_canvas)
        self.navigation_bar_container.setFixedSize(self.Configuration.dimension[0] - 60, 30)
        # self.navigation_bar_container.move(20, 20)
        self.navigation_bar_container.move(30, 20)
        
        action_bar = QWidget(self.navigation_bar_container)
        action_bar.setObjectName('navigationBar')
        action_bar.setFixedSize(40, 30)
        action_bar.move(self.Configuration.dimension[0] - 100, 0)
        
        exit_button = QPushButton(action_bar)
        exit_button.setObjectName('exitButton')
        exit_button.setFixedSize(20, 10)
        exit_button.move(10, 10)
        # exit_button.installEventFilter(self)
        exit_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        exit_button.clicked.connect(QCoreApplication.instance().quit)
        
        self.reload_button = QPushButton(self.navigation_bar_container)
        self.reload_button.setObjectName('primaryButton')
        self.reload_button.setFixedSize(30, 30)
        self.reload_button.setIcon(QIcon(".\\Images\\light-info.png"))
        self.reload_button.setStyleSheet("font-size: 10px;")
        self.reload_button.move(0, 0)
        self.reload_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.reload_button.cursor = Qt.CursorShape.PointingHandCursor
        self.reload_button.clicked.connect(self.createFileList)
        # self.reload_button.setEnabled(False)
        
        self.adaptive_bar = QLabel(self.navigation_bar_container)
        self.adaptive_bar.setObjectName('messageBar')
        self.adaptive_bar.setFixedSize(500, 30)
        self.adaptive_bar.move(self.Configuration.dimension[0] // 2 - 250, 0)
        self.adaptive_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.adaptive_bar.setCursor(Qt.CursorShape.SizeAllCursor)
        self.adaptive_bar.setText('Welcome to NORVA\'s Dev Environment!')
    
    
    
    def createFileList(self):
        
        try:
            self.primary_stacked_widget.removeWidget(self.file_list_scroll_area)
        except:
            pass
        
        self.file_list_scroll_area = QScrollArea(self.primary_stacked_widget)
        self.file_list_scroll_area.setObjectName('fileListScrollArea')
        # self.file_list_scroll_area.setFixedSize(self.Configuration.dimension[0] - 60, self.Configuration.dimension[1] - 70)
        self.file_list_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.file_list_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        file_list_container = QWidget(self.file_list_scroll_area)
        file_list_container.setObjectName('scrollableWidget')
        # file_list_container.setFixedSize(self.Configuration.dimension[0] - 60, self.Configuration.dimension[1] - 70)
        file_list_container_layout = QVBoxLayout(file_list_container)
        # file_list_container_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        file_list_container_layout.setContentsMargins(30, 30, 30, 30)
        file_list_container_layout.setSpacing(15)
        
        file_list = listdir('Data')
        for index, file in enumerate(file_list):
            
            file_container_widget = QWidget(file_list_container)
            file_container_widget.setObjectName('primaryContainer')
            file_container_widget.setFixedWidth(self.Configuration.dimension[0] - 60)
            # file_container_widget.setFixedWidth(self.Configuration.dimension[0] - 60)
            file_name_label = QLabel(file_container_widget)
            file_name_label.setObjectName('fileName')
            file_name_label.setStyleSheet("border-radius: 15px; color: #8DC63F;")
            file_name_label.setText(file)
            file_name_label.setFixedSize(220, 30)
            file_name_label.move(20, 20)
            file_index_label = QLabel(file_container_widget)
            file_index_label.setObjectName('fileIndex')
            file_size_label = QLabel(file_container_widget)
            file_size_label.setObjectName('fileName')
            file_size_label.setStyleSheet("border-radius: 15px; color: #8DC63F;")
            file_size_label.setText(str(path.getsize(f'Data\\{file}') / 1024) + ' KB')
            file_size_label.setFixedSize(100, 30)
            file_size_label.move(self.Configuration.dimension[0] - 180, 20)
            file_size_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            file_contents_label = QLabel(file_container_widget)
            file_contents_label.setObjectName('secondaryItemContainer')
            file_contents_label.setFixedWidth(self.Configuration.dimension[0] - 100)
            file_contents_label.setMinimumHeight(50)
            file_contents_label.setMaximumHeight(200)
            file_contents_label.move(20, 60)
            file_contents_label.setWordWrap(True)
            with open(f'Data\\{file}', 'rb') as stream:
                file_contents_label.setText(str(stream.read()))
            # print(file_contents_label.height())
            file_container_widget.setFixedHeight(240 + file_contents_label.height())
            
            file_list_container_layout.addWidget(file_container_widget)
        
        file_list_container.setLayout(file_list_container_layout)
        self.file_list_scroll_area.setWidget(file_list_container)
        self.primary_stacked_widget.addWidget(self.file_list_scroll_area)
        self.primary_stacked_widget.setCurrentWidget(self.file_list_scroll_area)
            
        





def initializeUI():
    
    Application = QApplication(sys.argv)
    ApplicationInitializer = UserInterface()
    ApplicationInitializer.show()
    sys.exit(Application.exec())





if __name__ == "__main__":  
    try:
        initializeUI()
    except Exception as error:
        print(error)