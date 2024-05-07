from os import mkdir, path, startfile
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
        self.initiateCommonVariables()
        self.initiateInstance()
        
        
        self.setStyleSheet(self.Configuration.stylesheet)
    
    
    
    def initiateCommonVariables(self):
        
        self.user_credentials = {
            'username': '', 
            'password': '', 
            'display_name': '', 
            'standing': '', 
            'status': 'active', 
            'allowed_storage': '', 
            'consumed_storage': ''
        }
        self.user_files = []
        
        self.interaction_selected_file = None
        self.interaction_selected_key_file = None
    
    
    
    
    def eventFilter(self, object, event):
        ...

    
    
    def initiateInstance(self):
        
        # Sets the background image for the application.
        background_image_pixmap = QPixmap(".\\Images\\wallpaper.jpg")
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
        
        # Initiates the DataHandler instance.
        self.DataHandler = DataHandler()
        
        # Creates the necessary pages for the application.
        self.createNavigationBar()
        self.createWelcomePage()
        self.createSignUpPage()
        self.createLoginPage()
    
    
    
    def showMessage(self, message, color = '#E43D25'):
            
            self.adaptive_bar.setText(message)
            self.adaptive_bar.setStyleSheet(f"color: {color};")
            # QTimer.singleShot(2500, lambda: self.adaptive_bar.setStyleSheet(f"color: {self.Configuration.accent['primary-text']};"), self.adaptive_bar.setText('Welcome to Contemlium Test Environment!'))
            
            # This will start a timer of 2.5 secs and set the color and message content to default.
            QTimer.singleShot(2500, lambda: [self.adaptive_bar.setStyleSheet(f"color: {self.Configuration.accent['primary-text']};"), self.adaptive_bar.setText('Welcome to Contemlium Test Environment!')])
    
    
    def createNavigationBar(self):
        
        self.navigation_bar_container = QWidget(self.base_canvas)
        self.navigation_bar_container.setFixedSize(self.Configuration.dimension[0] - 60, 30)
        # self.navigation_bar_container.move(20, 20)
        self.navigation_bar_container.move(30, 20)
        
        action_bar = QWidget(self.navigation_bar_container)
        action_bar.setObjectName('navigationBar')
        action_bar.setFixedSize(70, 30)
        action_bar.move(self.Configuration.dimension[0] - 130, 0)
        
        exit_button = QPushButton(action_bar)
        exit_button.setObjectName('exitButton')
        exit_button.setFixedSize(10, 10)
        exit_button.move(50, 10)
        # exit_button.installEventFilter(self)
        exit_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        exit_button.clicked.connect(QCoreApplication.instance().quit)
        
        self.theme_button = QPushButton(action_bar)
        self.theme_button.setObjectName('themeButton')
        self.theme_button.setFixedSize(10, 10)
        self.theme_button.move(10, 10)
        
        self.logout_button = QPushButton(action_bar)
        self.logout_button.setObjectName('logoutButton')
        self.logout_button.setFixedSize(10, 10)
        self.logout_button.move(30, 10)
        
        self.back_button = QPushButton(self.navigation_bar_container)
        self.back_button.setObjectName('primaryButton')
        self.back_button.setFixedSize(30, 30)
        # self.back_button.setText('◀')
        self.back_button.setIcon(QIcon(".\\Images\\light-info.png"))
        self.back_button.setStyleSheet("font-size: 10px;")
        self.back_button.move(0, 0)
        self.back_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.back_button.cursor = Qt.CursorShape.PointingHandCursor
        self.back_button.clicked.connect(self.clickBackButton)
        self.back_button.setEnabled(False)
        
        self.adaptive_bar = QLabel(self.navigation_bar_container)
        self.adaptive_bar.setObjectName('messageBar')
        self.adaptive_bar.setFixedSize(500, 30)
        self.adaptive_bar.move(self.Configuration.dimension[0] // 2 - 250, 0)
        self.adaptive_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.adaptive_bar.setCursor(Qt.CursorShape.SizeAllCursor)
        self.adaptive_bar.setText('Welcome to Contemlium Test Environment!')
    
    
    
    def createWelcomePage(self):
        
        self.welcome_page_widget = QWidget(self.primary_stacked_widget)
        
        logo_pixmap = QPixmap(".\\Images\\light-logo-medium.png")
        logo_pixmap = logo_pixmap.scaledToWidth(500)
        logo = QLabel(self.welcome_page_widget)
        logo.setPixmap(logo_pixmap)
        logo.setFixedSize(logo_pixmap.width(), logo_pixmap.height())
        logo.move(self.Configuration.dimension[0] // 2 - logo_pixmap.width() // 2, (self.Configuration.dimension[1] // 2 - logo_pixmap.height() // 2) - 70)
        self.primary_stacked_widget.addWidget(self.welcome_page_widget)
        
        login_button = QPushButton(self.welcome_page_widget)
        login_button.setObjectName('primaryButton')
        login_button.setFixedSize(150, 30)
        login_button.setFixedHeight(30)
        login_button.setText('SIGN INTO MY PROFILE')
        login_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        login_button.move(self.Configuration.dimension[0] // 2 + 10, self.Configuration.dimension[1] // 2 + 30)
        login_button.clicked.connect(self.clickLoginButton)
        
        sign_up_button = QPushButton(self.welcome_page_widget)
        sign_up_button.setObjectName('signUpButton')
        sign_up_button.setFixedSize(150, 30)
        sign_up_button.setFixedHeight(30)
        sign_up_button.setText('CREATE MY PROFILE')
        sign_up_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        sign_up_button.move(self.Configuration.dimension[0] // 2 - (150 + 10), self.Configuration.dimension[1] // 2 + 30)
        sign_up_button.clicked.connect(self.clickSignUpButton)
    
    
    
    def createSignUpPage(self):
        
        try:
            self.primary_stacked_widget.removeWidget(self.sign_up_page_widget)
        except:
            pass
        
        self.sign_up_page_widget = QWidget(self.primary_stacked_widget)
        
        container_widget = QWidget(self.sign_up_page_widget)
        container_widget.setObjectName('primaryContainer')
        container_widget.setFixedSize(500, 190)
        container_widget.move(self.Configuration.dimension[0] // 2 - 250, self.Configuration.dimension[1] // 2 - 150)
        
        username_field = QLineEdit(container_widget)
        username_field.setObjectName('primaryField')
        username_field.setFixedSize(200, 30)
        username_field.move(30, 30)
        username_field.setPlaceholderText('Here\'s my username...')
        username_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        display_name_field = QLineEdit(container_widget)
        display_name_field.setObjectName('primaryField')
        display_name_field.setFixedSize(200, 30)
        display_name_field.move(30, 80)
        display_name_field.setPlaceholderText('...but you can call me...')
        display_name_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        password_field = QLineEdit(container_widget)
        password_field.setObjectName('primaryField')
        password_field.setFixedSize(200, 30)
        password_field.move(30, 130)
        password_field.setPlaceholderText('Shh... It\'s a secret!')
        password_field.setEchoMode(QLineEdit.EchoMode.Password)
        password_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        sign_up_button = QPushButton(container_widget)
        sign_up_button.setObjectName('signUpButton')
        sign_up_button.setFixedSize(200, 50)
        sign_up_button.move(260, 70)
        sign_up_button.setText('Let\'s get started!')
        sign_up_button.setStyleSheet("font-size: 18px;")
        sign_up_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        sign_up_button.clicked.connect(lambda: self.clickSignUpButton({'username': username_field.text(), 'display_name': display_name_field.text(), 'password': password_field.text()}))
        
        self.primary_stacked_widget.addWidget(self.sign_up_page_widget)
    
    
    
    def createLoginPage(self):
        
        try:
            self.primary_stacked_widget.removeWidget(self.login_page_widget)
        except:
            pass
        
        self.login_page_widget = QWidget(self.primary_stacked_widget)
        
        container_widget = QWidget(self.login_page_widget)
        container_widget.setObjectName('primaryContainer')
        container_widget.setFixedSize(500, 140)
        container_widget.move(self.Configuration.dimension[0] // 2 - 250, self.Configuration.dimension[1] // 2 - 100)
        
        username_field = QLineEdit(container_widget)
        username_field.setObjectName('primaryField')
        username_field.setFixedSize(200, 30)
        username_field.move(30, 30)
        username_field.setPlaceholderText('Here\'s my username...')
        username_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        password_field = QLineEdit(container_widget)
        password_field.setObjectName('primaryField')
        password_field.setFixedSize(200, 30)
        password_field.move(30, 80)
        password_field.setPlaceholderText('Shh... It\'s a Secret!')
        password_field.setEchoMode(QLineEdit.EchoMode.Password)
        password_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        login_button = QPushButton(container_widget)
        login_button.setObjectName('loginButton')
        login_button.setFixedSize(200, 50)
        login_button.move(260, 45)
        login_button.setText('Log me in...')
        login_button.setStyleSheet("font-size: 18px;")
        login_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        login_button.clicked.connect(lambda: self.clickLoginButton({'username': username_field.text(), 'password': password_field.text()}))
        
        self.primary_stacked_widget.addWidget(self.login_page_widget)
    
    
    
    def createHomePage(self):
        
        try:
            self.primary_stacked_widget.removeWidget(self.home_page_widget)
        except:
            pass
        
        self.home_page_widget = QWidget(self.primary_stacked_widget)
        
        side_bar_widget = QWidget(self.home_page_widget)
        side_bar_widget.setObjectName('sideBarWidget')
        side_bar_widget.setFixedSize(300, self.Configuration.dimension[1] - 130)
        side_bar_widget.move(30, 30)
        
        logo_pixmap = QPixmap(".\\Images\\light-logo-small.png")
        logo_pixmap = logo_pixmap.scaledToWidth(150)
        logo = QLabel(side_bar_widget)
        logo.setPixmap(logo_pixmap)
        logo.setFixedSize(logo_pixmap.width(), logo_pixmap.height())
        # logo.move(self.Configuration.dimension[0] // 2 - logo_pixmap.width() // 2, (self.Configuration.dimension[1] // 2 - logo_pixmap.height() // 2) - 70)
        logo.move(75, 40)
        
        self.display_name_label = QLineEdit(side_bar_widget)
        self.display_name_label.setObjectName('primaryField')
        self.display_name_label.setFixedSize(200, 30)
        self.display_name_label.move(50, 120)
        self.display_name_label.setText(self.user_credentials['display_name'])
        self.display_name_label.setStyleSheet("font-family: 'Impact'; font-size: 12px;")

        self.display_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.display_name_label.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        
        show_stats_button = QPushButton(side_bar_widget)
        show_stats_button.setObjectName('itemButton')
        show_stats_button.setFixedSize(20, 20)
        show_stats_button.move(95, 170)
        show_stats_button.setIcon(QIcon(".\\Images\\light-stats.png"))
        show_stats_button.setCursor(Qt.CursorShape.PointingHandCursor)
        show_stats_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        show_stats_button.clicked.connect(self.switchToInfoPanel)
        
        change_display_name_button = QPushButton(side_bar_widget)
        change_display_name_button.setObjectName('itemButton')
        change_display_name_button.setFixedSize(20, 20)
        change_display_name_button.move(125, 170)
        change_display_name_button.setIcon(QIcon(".\\Images\\light-edit.png"))
        change_display_name_button.setCursor(Qt.CursorShape.PointingHandCursor)
        change_display_name_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        change_display_name_button.clicked.connect(self.clickChangeDisplayNameButton)
        
        change_password_button = QPushButton(side_bar_widget)
        change_password_button.setObjectName('itemButton')
        change_password_button.setFixedSize(20, 20)
        change_password_button.move(155, 170)
        change_password_button.setIcon(QIcon(".\\Images\\light-password.png"))
        change_password_button.setCursor(Qt.CursorShape.PointingHandCursor)
        change_password_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        
        delete_user_button = QPushButton(side_bar_widget)
        delete_user_button.setObjectName('itemButton')
        delete_user_button.setFixedSize(20, 20)
        delete_user_button.move(185, 170)
        delete_user_button.setIcon(QIcon(".\\Images\\delete.png"))
        delete_user_button.setCursor(Qt.CursorShape.PointingHandCursor)
        delete_user_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        
        
        self.interaction_stacked_widget = QStackedWidget(side_bar_widget)
        self.interaction_stacked_widget.setFixedSize(260, self.Configuration.dimension[1] - 420)
        self.interaction_stacked_widget.move(20, 200)
        
        self.switchToInfoPanel()
        
        upload_file_button = QPushButton(side_bar_widget)
        upload_file_button.setObjectName('primaryField')
        upload_file_button.setFixedSize(180, 30)
        upload_file_button.move(60, self.Configuration.dimension[1] - 190)
        upload_file_button.setText('Upload a file...')
        upload_file_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        upload_file_button.clicked.connect(self.switchToUploadPanel)
        
        self.file_list_container = QStackedWidget(self.home_page_widget)
        # file_list_container.setObjectName('secondaryContainer')
        self.file_list_container.setFixedSize(910, self.Configuration.dimension[1] - 130)
        self.file_list_container.move(360, 30)
        
        self.createFileList()
        
        self.primary_stacked_widget.addWidget(self.home_page_widget)
    
    
    
    def switchToInfoPanel(self):
        
        try:
            self.interaction_stacked_widget.removeWidget(self.info_panel_widget)
        except:
            pass
        
        self.info_panel_widget = QWidget(self.interaction_stacked_widget)
        self.info_panel_widget.setObjectName('secondaryContainer')
        self.info_panel_widget.setFixedSize(260, self.Configuration.dimension[1] - 450)
        # self.info_panel_widget.move(30, 230)
        
        status_color = {
            'active': '#8DC63F', 
            'suspended': '#E43D25'
        }
        status_container = QWidget(self.info_panel_widget)
        status_container.setObjectName('secondaryItemContainer')
        status_container.setFixedSize(75, 30)
        status_container.move(30, 30)
        status_label = QLabel(status_container)
        # status_label.setObjectName('itemLabel')
        status_label.setStyleSheet("color: #BEB3D8; font-family: 'Nirmala UI'; font-size: 10px;")
        status_label.setFixedHeight(30)
        status_label.move(10, 0)
        status_label.setText('STATUS')
        status_widget = QWidget(status_container)
        status_widget.setStyleSheet(f"background-color: {status_color[self.user_credentials['status']]}; border-radius: 5px;")
        status_widget.setFixedSize(10, 10)
        status_widget.move(55, 10)
        
        standings_container = QWidget(self.info_panel_widget)
        standings_container.setObjectName('secondaryItemContainer')
        standings_container.setFixedSize(40, 30)
        standings_container.move(190, 30)
        standings_container.setToolTip('Your standing in the organization.')
        standings_label = QLabel(standings_container)
        standings_label.setObjectName('itemLabel')
        standings_label.setFixedHeight(30)
        standings_label.move(10, 0)
        standings_label.setText(str(self.user_credentials['standing']))
        
        storage_container = QWidget(self.info_panel_widget)
        storage_container.setObjectName('secondaryItemContainer')
        storage_container.setFixedSize(200, 70)
        storage_container.move(30, 70)
        total_storage_bar = QWidget(storage_container)
        total_storage_bar.setObjectName('primaryItemContainer')
        total_storage_bar.setStyleSheet("border-radius: 5px;")
        total_storage_bar.setFixedSize(120, 10)
        total_storage_bar.move(10, 20)
        used_storage_bar = QWidget(total_storage_bar)
        used_storage_bar.setStyleSheet("border-radius: 5px; background-color: #8DC63F;")
        width = int(self.user_credentials['consumed_storage']) / int(self.user_credentials['allowed_storage'])
        used_storage_bar.setFixedSize(10 + int(width * 120), 10)
        used_storage_bar.move(-10, 0)
        storage_percentage_label = QLabel(storage_container)
        storage_percentage_label.setObjectName('primaryItemContainer')
        storage_percentage_label.setStyleSheet("border-radius: 10px;")
        storage_percentage_label.setFixedSize(50, 20)
        storage_percentage_label.move(140, 15)
        storage_percentage_label.setText(f"{round(width * 100, 2)}%")
        storage_percentage_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.interaction_stacked_widget.addWidget(self.info_panel_widget)
        self.interaction_stacked_widget.setCurrentWidget(self.info_panel_widget)
    
    
    
    def switchToUploadPanel(self):
        
        self.interaction_selected_file = None
        self.attained_atleast_once = False
            
        try:
            self.interaction_stacked_widget.removeWidget(self.upload_panel_widget)
        except:
            pass
        
        self.upload_panel_widget = QWidget(self.interaction_stacked_widget)
        self.upload_panel_widget.setObjectName('secondaryContainer')
        self.upload_panel_widget.setFixedSize(260, self.Configuration.dimension[1] - 470)
        # self.upload_panel_widget.move(30, 230)
        
        # upload_container = QWidget(self.upload_panel_widget)
        # upload_container.setObjectName('secondaryItemContainer')
        # upload_container.setFixedSize(200, 30)
        # upload_container.move(30, 30)
        self.interaction_choose_button = QPushButton(self.upload_panel_widget)
        self.interaction_choose_button.setObjectName('secondaryItemContainer')
        self.interaction_choose_button.setFixedSize(200, 30)
        self.interaction_choose_button.move(30, 30)
        self.interaction_choose_button.setText('Please select a file to continue...')
        self.interaction_choose_button.setToolTip('Click to select a file.')
        self.interaction_choose_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.interaction_choose_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.interaction_choose_button.clicked.connect(lambda: self.clickInteractionSelectFileButton())
        self.interaction_file_password_field = QLineEdit(self.upload_panel_widget)
        self.interaction_file_password_field.setObjectName('secondaryItemContainer')
        self.interaction_file_password_field.setFixedSize(140, 30)
        self.interaction_file_password_field.move(30, 70)
        self.interaction_file_password_field.setPlaceholderText('Password for the file...')
        self.interaction_file_password_field.setEchoMode(QLineEdit.EchoMode.Password)
        self.interaction_file_password_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.interaction_file_password_field.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.interaction_file_password_field.setToolTip('[Optional] Password for the file.')
        self.fragment_size_field = QLineEdit(self.upload_panel_widget)
        self.fragment_size_field.setObjectName('secondaryItemContainer')
        self.fragment_size_field.setFixedSize(50, 30)
        self.fragment_size_field.move(180, 70)
        self.fragment_size_field.setPlaceholderText('Size')
        self.fragment_size_field.setText('512')
        self.fragment_size_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.fragment_size_field.setToolTip('Lower (64): Secure; Higher (5120000): Faster interactions.')
        self.get_fragment_button = QPushButton(self.upload_panel_widget)
        self.get_fragment_button.setObjectName('secondaryItemContainer')
        self.get_fragment_button.setFixedSize(140, 30)
        # self.get_fragment_button.move(30, 110)
        self.get_fragment_button.move(60, 110)
        self.get_fragment_button.setText('Attain file key...')
        self.get_fragment_button.setToolTip('Click to attain the key for the file.')
        self.get_fragment_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.get_fragment_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.get_fragment_button.setDisabled(True)
        self.interaction_upload_button = QPushButton(self.upload_panel_widget)
        self.interaction_upload_button.setObjectName('actionButton')
        self.interaction_upload_button.setFixedSize(200, 30)
        self.interaction_upload_button.move(30, 170)
        self.interaction_upload_button.setText('Upload it!')
        self.interaction_upload_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.interaction_upload_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        # self.interaction_upload_button.clicked.connect(lambda: self.DataHandler.uploadFile(self.interaction_selected_file, self.interaction_file_password_field.text(), self.user_credentials))
        self.interaction_upload_button.clicked.connect(lambda: self.clickUploadButton())
        
        self.interaction_stacked_widget.addWidget(self.upload_panel_widget)
        self.interaction_stacked_widget.setCurrentWidget(self.upload_panel_widget)
    
    
    
    def switchToOpenPanel(self, index):
        
        self.interaction_selected_key_file = None
        
        try:
            self.interaction_stacked_widget.removeWidget(self.open_panel_widget)
        except:
            pass
        
        self.open_panel_widget = QWidget(self.interaction_stacked_widget)
        self.open_panel_widget.setObjectName('secondaryContainer')
        self.open_panel_widget.setFixedSize(260, self.Configuration.dimension[1] - 470)
        # self.open_panel_widget.move(30, 230)
        
        self.key_file_button = QPushButton(self.open_panel_widget)
        self.key_file_button.setObjectName('secondaryItemContainer')
        self.key_file_button.setFixedSize(200, 30)
        self.key_file_button.move(30, 30)
        self.key_file_button.setText('Please provide the key file...')
        self.key_file_button.setToolTip('Click to select the key file.')
        self.key_file_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.key_file_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.key_file_button.clicked.connect(lambda: self.clickInteractionsSelectKeyFileButton())
        
        self.key_file_password_field = QLineEdit(self.open_panel_widget)
        self.key_file_password_field.setObjectName('secondaryItemContainer')
        self.key_file_password_field.setFixedSize(200, 30)
        self.key_file_password_field.move(30, 70)
        self.key_file_password_field.setPlaceholderText('Password for the key file...')
        self.key_file_password_field.setEchoMode(QLineEdit.EchoMode.Password)
        self.key_file_password_field.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.key_file_password_field.setToolTip('Password for the key file.')
        self.key_file_password_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.user_password_field = QLineEdit(self.open_panel_widget)
        self.user_password_field.setObjectName('secondaryItemContainer')
        self.user_password_field.setFixedSize(200, 30)
        self.user_password_field.move(30, 110)
        self.user_password_field.setPlaceholderText('Your password...')
        self.user_password_field.setEchoMode(QLineEdit.EchoMode.Password)
        self.user_password_field.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.user_password_field.setToolTip('Please provide the password you used to sign up.')
        self.user_password_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.interaction_open_button = QPushButton(self.open_panel_widget)
        self.interaction_open_button.setObjectName('actionButton')
        self.interaction_open_button.setFixedSize(200, 30)
        self.interaction_open_button.move(30, 170)
        self.interaction_open_button.setText('Open it!')
        self.interaction_open_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.interaction_open_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.interaction_open_button.clicked.connect(lambda: self.clickOpenButton(index))
        # open_button.clicked.connect(lambda: self.showMessage('File opened successfully!', '#8DC63F'))
        
        self.interaction_stacked_widget.addWidget(self.open_panel_widget)
        self.interaction_stacked_widget.setCurrentWidget(self.open_panel_widget)
    
    
    
    def switchToDeletePanel(self, index):
        
        self.interaction_selected_key_file = None
        
        try:
            self.interaction_stacked_widget.removeWidget(self.delete_panel_widget)
        except:
            pass
        
        self.delete_panel_widget = QWidget(self.interaction_stacked_widget)
        self.delete_panel_widget.setObjectName('secondaryContainer')
        self.delete_panel_widget.setFixedSize(260, self.Configuration.dimension[1] - 440)
        # self.delete_panel_widget.move(30, 230)
        
        self.key_file_button = QPushButton(self.delete_panel_widget)
        self.key_file_button.setObjectName('secondaryItemContainer')
        self.key_file_button.setFixedSize(200, 30)
        self.key_file_button.move(30, 30)
        self.key_file_button.setText('Please provide the key file...')
        self.key_file_button.setToolTip('Click to select the key file.')
        self.key_file_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.key_file_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.key_file_button.clicked.connect(lambda: self.clickInteractionsSelectKeyFileButton())
        
        self.key_file_password_field = QLineEdit(self.delete_panel_widget)
        self.key_file_password_field.setObjectName('secondaryItemContainer')
        self.key_file_password_field.setFixedSize(200, 30)
        self.key_file_password_field.move(30, 70)
        self.key_file_password_field.setPlaceholderText('Password for the key file...')
        self.key_file_password_field.setEchoMode(QLineEdit.EchoMode.Password)
        self.key_file_password_field.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.key_file_password_field.setToolTip('Password for the key file.')
        self.key_file_password_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        delete_warning_label = QLabel(self.delete_panel_widget)
        delete_warning_label.setObjectName('deleteButton')
        delete_warning_label.setFixedSize(200, 45)
        delete_warning_label.setText("WARNING: This action cannot be undone.")
        delete_warning_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        delete_warning_label.setWordWrap(True)
        delete_warning_label.move(30, 130)
        
        self.interaction_delete_button = QPushButton(self.delete_panel_widget)
        self.interaction_delete_button.setObjectName('actionButton')
        self.interaction_delete_button.setFixedSize(200, 30)
        self.interaction_delete_button.move(30, 200)
        self.interaction_delete_button.setText('Delete it!')
        name = self.user_files[index]['name']
        self.interaction_delete_button.setToolTip(f"This action will delete '{name}' and will render it unrecoverable.")
        self.interaction_delete_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.interaction_delete_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.interaction_delete_button.clicked.connect(lambda: self.clickDeleteButton(index))
        
        self.interaction_stacked_widget.addWidget(self.delete_panel_widget)
        self.interaction_stacked_widget.setCurrentWidget(self.delete_panel_widget)
    
    
    
    def createFileList(self):
        
        if len(self.user_files) == 0:
            ...
        else:
            
            try:
                self.file_list_container.removeWidget(self.file_list_container.currentWidget())
            except:
                pass
            
            file_list_scroll_area = QScrollArea(self.file_list_container)
            file_list_scroll_area.setFixedSize(910, self.Configuration.dimension[1] - 130)
            file_list_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
            file_list_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
            
            file_list_container_widget = QWidget(file_list_scroll_area)
            file_list_container_widget.setObjectName('scrollableWidget')
            file_list_container_layout = QVBoxLayout(file_list_container_widget)
            file_list_container_layout.setContentsMargins(0, 0, 0, 0)
            file_list_container_layout.setSpacing(10)
            
            for index, file in enumerate(self.user_files):
                
                file_container = QWidget(file_list_container_widget)
                file_container.setObjectName('primaryContainer')
                file_container.setFixedSize(910, 90)
                file_extension_label = QLabel(file_container)
                file_extension_label.setObjectName('fileExtension')
                file_extension_label.setFixedSize(50, 20)
                file_extension_label.move(10, 10)
                file_extension_label.setText(file['extension'].upper())
                file_extension_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                file_name_label = QLabel(file_container)
                file_name_label.setObjectName('fileName')
                file_name_label.setFixedSize(630, 20)
                file_name_label.move(80, 10)
                file_name_label.setText(file['name'])
                file_name_label.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
                file_size_label = QLabel(file_container)
                file_size_label.setObjectName('fileName')
                file_size_label.setFixedSize(50, 20)
                file_size_label.move(720, 10)
                file_size_label.setText(str(round(file['size'] / 1024, 2)) + " GB")
                file_upload_date_label = QLabel(file_container)
                file_upload_date_label.setObjectName('uploadDate')
                file_upload_date_label.setFixedSize(80, 20)
                file_upload_date_label.move(820, 10)
                file_upload_date_label.setText(file['date'])
                file_upload_date_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                
                file_delete_button = QPushButton(file_container)
                file_delete_button.setObjectName('deleteButton')
                file_delete_button.setFixedSize(70, 30)
                file_delete_button.move(10, 50)
                file_delete_button.setText('DELETE')
                file_delete_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
                file_delete_button.clicked.connect(lambda: self.switchToDeletePanel(index))
                # file_delete_button.clicked.connect(lambda: self.DataHandler.deleteFile(file['name'], self.user_credentials))
                file_cancel_button = QPushButton(file_container)
                file_cancel_button.setObjectName('actionButton')
                file_cancel_button.setFixedSize(70, 30)
                file_cancel_button.move(100, 50)
                file_cancel_button.setText('CANCEL')
                file_cancel_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
                file_cancel_button.clicked.connect(lambda: [self.showMessage('File action cancelled.'), self.interaction_stacked_widget.setCurrentWidget(self.info_panel_widget)])
                file_rename_button = QPushButton(file_container)
                file_rename_button.setObjectName('actionButton')
                file_rename_button.setFixedSize(70, 30)
                file_rename_button.move(740, 50)
                file_rename_button.setText('RENAME')
                file_rename_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
                # file_rename_button.clicked.connect(lambda: self.DataHandler.renameFile(file['name'], self.user_credentials))
                file_open_button = QPushButton(file_container)
                file_open_button.setObjectName('actionButton')
                file_open_button.setFixedSize(70, 30)
                file_open_button.move(830, 50)
                file_open_button.setText('OPEN')
                file_open_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
                # file_open_button.clicked.connect(lambda: self.DataHandler.openFile(file['name'], self.user_credentials))
                file_open_button.clicked.connect(lambda: self.switchToOpenPanel(index))
                
                file_list_container_layout.addWidget(file_container)
            
            file_list_container_widget.setLayout(file_list_container_layout)
            file_list_scroll_area.setWidget(file_list_container_widget)
            self.file_list_container.addWidget(file_list_scroll_area)
            self.file_list_container.setCurrentWidget(file_list_scroll_area)
    
    
    
    def clickBackButton(self):
        
        if self.primary_stacked_widget.currentWidget() in [self.login_page_widget, self.sign_up_page_widget]:
            self.primary_stacked_widget.setCurrentWidget(self.welcome_page_widget)
            self.back_button.setIcon(QIcon(".\\Images\\light-info.png"))
            self.back_button.setEnabled(False)
        elif self.primary_stacked_widget.currentWidget() == self.home_page_widget:
            self.primary_stacked_widget.setCurrentWidget(self.welcome_page_widget)
            self.back_button.setIcon(QIcon(".\\Images\\light-info.png"))
            self.back_button.setEnabled(False)
        else:
            pass
    
    
    
    def clickSignUpButton(self, user_credentials = {}):
        
        if self.primary_stacked_widget.currentWidget() == self.welcome_page_widget:
            self.initiateCommonVariables()
            self.createSignUpPage()
            self.primary_stacked_widget.setCurrentWidget(self.sign_up_page_widget)
            
            self.back_button.setIcon(QIcon(".\\Images\\light-home.png"))
            self.back_button.setEnabled(True)
            return
        
        error_codes = {
            '0': 'You are not connected to the internet. Please try again.', 
            '1': 'It is necessary to fill all the fields. Please try again.', 
            '2': 'Username already exists. Please try another one.'
        }
        
        dump = self.DataHandler.createAccount(user_credentials)
        if isinstance(dump, str) and dump in error_codes:
            print(error_codes[dump])
            self.showMessage(error_codes[dump])
        else:
            for key in dump:
                if key in self.user_credentials:
                    self.user_credentials[key] = dump[key]
            self.user_files = dump['files']
            self.showMessage('Account created successfully!', '#8DC63F')
            self.createHomePage()
            self.back_button.setIcon(QIcon(".\\Images\\light-back.png"))
            self.primary_stacked_widget.setCurrentWidget(self.home_page_widget)
            print("Account created successfully.")
    
    
    
    def clickLoginButton(self, user_credentials = {}):
        
        if self.primary_stacked_widget.currentWidget() == self.welcome_page_widget:
            self.initiateCommonVariables()
            self.createLoginPage()
            self.primary_stacked_widget.setCurrentWidget(self.login_page_widget)
            
            self.back_button.setIcon(QIcon(".\\Images\\light-home.png"))
            self.back_button.setEnabled(True)
            return
        
        error_codes = {
            '0': 'You are not connected to the internet. Please try again.', 
            '1': 'One or more of your credential(s) is incorrect. Please try again.', 
            '2': 'User does not exist. Please sign up.', 
            '3': 'User is under suspension. Please contact support.'
        }
        
        dump = self.DataHandler.loginAccount(user_credentials)
        if isinstance(dump, str) and dump in error_codes:
            print(error_codes[dump])
            self.showMessage(error_codes[dump])
        else:
            for key in dump:
                if key in self.user_credentials:
                    self.user_credentials[key] = dump[key]
            self.user_files = dump['files']
            self.showMessage('Logged in successfully!', '#8DC63F')
            self.createHomePage()
            self.back_button.setIcon(QIcon(".\\Images\\light-back.png"))
            self.primary_stacked_widget.setCurrentWidget(self.home_page_widget)
            print("Logged in successfully.")
    
    
    
    def clickChangeDisplayNameButton(self):
        
        if self.DataHandler.updateDisplayName(self.display_name_label.text(), self.user_credentials['username']):
            self.showMessage('Display name updated successfully!', '#8DC63F')
            print("Display name updated successfully.")
            self.display_name_label.clearFocus()
            self.user_credentials['display_name'] = self.display_name_label.text()
        else:
            self.showMessage('Display name could not be updated. Please try again.')
            print("Display name could not be updated.")
            self.display_name_label.setText(self.user_credentials['display_name'])
        
    
    
    def clickDeleteUserButton(self):
        
        ...
    
    
    
    def clickInteractionSelectFileButton(self):

        Tk().withdraw()
        
        file = filedialog.askopenfile()
        if file:
            self.interaction_selected_file = file
            self.interaction_choose_button.setText(file.name.split('/')[-1])
            self.interaction_choose_button.setToolTip(file.name.split('/')[-1])
            self.showMessage('File selected successfully!', '#8DC63F')
        else:
            self.showMessage('File selection cancelled.')
    
    
    
    def clickUploadButton(self):
        
        if self.interaction_selected_file is None:
            self.showMessage('Please select a file to upload.')
            return
        else:
            error_codes = {
                '0': 'You are not connected to the internet. Please try again.', 
                '1': 'One or more of your credential(s) is incorrect. Please try again.', 
                '2': 'User does not exist. Please sign up.', 
                '3': 'User is under suspension. Please contact support.', 
                '4': 'You do not have enough storage to upload this file.'
            }
            
            fragment_size = int(self.fragment_size_field.text())
            if fragment_size < 64:
                self.showMessage('Fragment size is too low. Please try again.')
                return
            elif fragment_size > 5120000:
                self.showMessage('Fragment size is too high. Please try again.')
                return
            result = self.DataHandler.uploadFile(self.interaction_selected_file, self.interaction_file_password_field.text(), int(self.fragment_size_field.text()), {'username': self.user_credentials['username'], 'password': self.user_credentials['password']}, self.user_files, self.user_credentials['consumed_storage'], self.user_credentials['allowed_storage'])
            if isinstance(result, str) and result in error_codes:
                print(error_codes[result])
                self.showMessage(error_codes[result])
            else:
                self.user_files = result[0]
                self.user_credentials['consumed_storage'] = result[1]
                
                self.interaction_upload_button.setDisabled(False)
                self.interaction_upload_button.setText('Close this page')
                self.interaction_upload_button.setToolTip('You are required to save the key file atleast once to be able to close this page.')
                self.interaction_upload_button.clicked.disconnect()
                self.interaction_upload_button.clicked.connect(lambda: self.showMessage('You are required to save the key file atleast once to be able to close this page.'))
                
                encrypted_fragment_file = result[2]
                self.get_fragment_button.clicked.connect(lambda: self.clickAttainFragmentFileButton(encrypted_fragment_file))
                self.get_fragment_button.setDisabled(False)
                
                
                # if self.attained_atleast_once:
                #     self.showMessage('File uploaded successfully!', '#8DC63F')
                #     self.createFileList()
                #     self.switchToInfoPanel()
    
    
    
    def clickAttainFragmentFileButton(self, encrypted_fragment_file):
        
        Tk().withdraw()
        
        # take the save location from the user with the extension .fmt
        save_location = filedialog.asksaveasfilename(defaultextension = '.fmt', filetypes = [('Fragment File', '*.fmt')])
        
        if save_location:
            
            # code to save the encrypted fragment file as .fmt file in th esave_location
            with open(save_location, 'wb') as file:
                file.write(encrypted_fragment_file)
            
            self.attained_atleast_once = True
            # self.interaction_upload_button.setDisabled(True)
            self.interaction_upload_button.setText('Close this page')
            self.interaction_upload_button.setToolTip('Close this page and return to the home page.')
            self.interaction_upload_button.clicked.disconnect()
            self.interaction_upload_button.clicked.connect(lambda: [self.showMessage('File uploaded successfully!', '#8DC63F'), self.createFileList(), self.switchToInfoPanel()])
        else:
            self.showMessage('Fragment file save cancelled.')
            return
        
        ...
    
    
    
    def clickInteractionsSelectKeyFileButton(self):
        
        Tk().withdraw()
        file = filedialog.askopenfile()
            
        if file:
            
            self.interaction_selected_key_file = file
            self.key_file_button.setText(file.name.split('/')[-1])
            self.key_file_button.setToolTip(file.name.split('/')[-1])
            self.showMessage('Key file selected successfully!', '#8DC63F')
        else:
            self.showMessage('Key file selection cancelled.')
    
    
    
    def clickOpenButton(self, index):
        
        if self.interaction_selected_key_file is None:
            self.showMessage('Please select a key file to open the file.')
            return
        else:
            error_codes = {
                '0': 'You are not connected to the internet. Please try again.', 
                '1': 'One or more of your credential(s) is incorrect. Please try again.', 
                '2': 'You provided an incorrect key file. Please try again.', 
                '3': 'One or more of the fragments are missing. Please try again.', 
                '4': 'One or more of the fragments are corrupted. Please try again.'
            }
        
        with open(self.interaction_selected_key_file.name, 'rb') as stream:
            key_file = stream.read()
        
        result = self.DataHandler.openFile(key_file, self.key_file_password_field.text(), {'username': self.user_credentials['username'], 'password': self.user_credentials['password']}, self.user_files[index])
        if isinstance(result, str) and result in error_codes:
            print(error_codes[result])
            self.showMessage(error_codes[result])
        else:
            
            save_location = filedialog.asksaveasfilename(defaultextension = self.user_files[index]['extension'], filetypes = [(self.user_files[index]['extension'].upper() + ' File', '*' + self.user_files[index]['extension'])])
            with open(save_location, 'wb') as file:
                file.write(result)
            
            # Code to open the file in a window
            with open(save_location, 'rb') as file:
                file_data = file.read()

            if path.exists(save_location):
                startfile(save_location)
            
            self.showMessage('File opened successfully!', '#8DC63F')
            self.interaction_stacked_widget.setCurrentWidget(self.info_panel_widget)
    
    
    
    def clickDeleteButton(self, index):
        
        if self.interaction_selected_key_file is None:
            self.showMessage('Please select a key file to open the file.')
            return
        else:
            error_codes = {
                '0': 'You are not connected to the internet. Please try again.', 
                '1': 'One or more of your credential(s) is incorrect. Please try again.', 
                '2': 'You provided an incorrect key file. Please try again.', 
                '3': 'One or more of the fragments are missing. Please try again.', 
                '4': 'One or more of the fragments are corrupted. Please try again.'
            }
        
        result = self.DataHandler.deleteFile(self.interaction_selected_key_file, self.interaction_file_password_field.text(), {'username': self.user_credentials, 'password': self.user_credentials['password']}, self.user_files, index)
        # result = self.DataHandler.deleteFile(self.interaction_selected_key_file, self.key_file_password_field.text(), self.user_credentials['username'], self.user_files, index)
        if isinstance(result, str) and result in error_codes:
            print(error_codes[result])
            self.showMessage(error_codes[result])
        else:
            ...
            self.showMessage('File deleted successfully!', '#8DC63F')
            self.interaction_stacked_widget.setCurrentWidget(self.info_panel_widget)
        






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