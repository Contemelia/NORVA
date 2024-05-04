from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
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
    
    
    
    def eventFilter(self, object, event):
        ...

    
    
    def initiateInstance(self):
        
        background_image_pixmap = QPixmap(".\\Images\\wallpaper.jpg")
        background_image = QLabel(self)
        background_image.setGeometry(0, 0, self.Configuration.dimension[0], self.Configuration.dimension[1])
        background_image.setPixmap(background_image_pixmap)
        
        self.base_canvas = QWidget(self)
        self.base_canvas.setObjectName('baseCanvas')
        self.base_canvas.setGeometry(0, 0, self.Configuration.dimension[0], self.Configuration.dimension[1])
        # self.baseLayout = QStackedLayout(self.base_canvas)
        
        self.primary_stacked_widget = QStackedWidget(self.base_canvas)
        self.primary_stacked_widget.setObjectName('primaryStackedWidget')
        self.primary_stacked_widget.setFixedSize(self.Configuration.dimension[0], self.Configuration.dimension[1] - 70)
        self.primary_stacked_widget.move(0, 70)
        # self.primary_stacked_layout = QStackedLayout(self.primary_stacked_widget)
        
        self.DataHandler = DataHandler()
        
        self.createNavigationBar()
        self.createWelcomePage()
        self.createSignUpPage()
        self.createLoginPage()
    
    
    
    def setPage(self, page):
        ...
    
    
    
    def createNavigationBar(self):
        
        self.navigation_bar_container = QWidget(self.base_canvas)
        # self.navigation_bar_container.setObjectName('navigationBar')
        self.navigation_bar_container.setFixedSize(self.Configuration.dimension[0] - 40, 30)
        self.navigation_bar_container.move(20, 20)
        
        action_bar = QWidget(self.navigation_bar_container)
        action_bar.setObjectName('navigationBar')
        action_bar.setFixedSize(70, 30)
        action_bar.move(self.Configuration.dimension[0] - 110, 0)
        
        exit_button = QPushButton(action_bar)
        exit_button.setObjectName('exitButton')
        exit_button.setFixedSize(10, 10)
        exit_button.move(30, 10)
        # exit_button.installEventFilter(self)
        exit_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        exit_button.clicked.connect(QCoreApplication.instance().quit)
        
        self.theme_button = QPushButton(action_bar)
        self.theme_button.setObjectName('themeButton')
        self.theme_button.setFixedSize(10, 10)
        self.theme_button.move(10, 10)
        
        back_button = QPushButton(self.navigation_bar_container)
        back_button.setObjectName('primaryButton')
        back_button.setFixedSize(30, 30)
        back_button.setText('௹')
        back_button.move(0, 0)
        back_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        back_button.cursor = Qt.CursorShape.PointingHandCursor
        back_button.clicked.connect(self.clickBackButton)
    
    
    
    def createWelcomePage(self):
        
        self.welcome_page_widget = QWidget(self.primary_stacked_widget)
        
        logo_pixmap = QPixmap(".\\Images\\full-logo-white.png")
        logo_pixmap = logo_pixmap.scaledToWidth(500)
        logo = QLabel(self.welcome_page_widget)
        logo.setPixmap(logo_pixmap)
        logo.setFixedSize(logo_pixmap.width(), logo_pixmap.height())
        logo.move(self.Configuration.dimension[0] // 2 - logo_pixmap.width() // 2, (self.Configuration.dimension[1] // 2 - logo_pixmap.height() // 2) - 70)
        self.primary_stacked_widget.addWidget(self.welcome_page_widget)
        # self.primary_stacked_widget.setCurrentWidget(self.welcome_page_widget)
        
        login_button = QPushButton(self.welcome_page_widget)
        login_button.setObjectName('loginButton')
        login_button.setFixedSize(150, 30)
        login_button.setFixedHeight(30)
        login_button.setText('SIGN INTO MY PROFILE')
        login_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        login_button.AllignmentFlag = Qt.AlignmentFlag.AlignCenter
        login_button.move(self.Configuration.dimension[0] // 2 + 10, self.Configuration.dimension[1] // 2 + 30)
        login_button.clicked.connect(self.clickLoginButton)
        
        sign_up_button = QPushButton(self.welcome_page_widget)
        sign_up_button.setObjectName('signUpButton')
        sign_up_button.setFixedSize(150, 30)
        sign_up_button.setFixedHeight(30)
        sign_up_button.setText('CREATE MY PROFILE')
        sign_up_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        sign_up_button.AllignmentFlag = Qt.AlignmentFlag.AlignCenter
        sign_up_button.move(self.Configuration.dimension[0] // 2 - (150 + 10), self.Configuration.dimension[1] // 2 + 30)
        sign_up_button.clicked.connect(self.clickSignUpButton)
    
    
    
    def createSignUpPage(self):
        
        try:
            self.primary_stacked_widget.removeWidget(self.sign_up_page_widget)
        except:
            pass
        
        self.sign_up_page_widget = QWidget(self.primary_stacked_widget)
        
        container_widget = QWidget(self.sign_up_page_widget)
        container_widget.setObjectName('containerWidget')
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
        container_widget.setObjectName('containerWidget')
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
    
    
    
    def clickBackButton(self):
        
        if self.primary_stacked_widget.currentWidget() == self.login_page_widget:
            self.primary_stacked_widget.setCurrentWidget(self.welcome_page_widget)
        elif self.primary_stacked_widget.currentWidget() == self.sign_up_page_widget:
            self.primary_stacked_widget.setCurrentWidget(self.welcome_page_widget)
        else:
            pass
    
    
    
    def clickSignUpButton(self, user_credentials = {}):
        
        if self.primary_stacked_widget.currentWidget() == self.welcome_page_widget:
            self.initiateCommonVariables()
            self.createSignUpPage()
            self.primary_stacked_widget.setCurrentWidget(self.sign_up_page_widget)
            return
        
        error_codes = {
            '0': False, 
            '1': 'Username already exists. Please try another one.'
        }
        
        dump = self.DataHandler.createAccount(user_credentials)
        if isinstance(dump, str) and dump in error_codes:
            print(error_codes[dump])
        else:
            for key in dump:
                if key in self.user_credentials:
                    self.user_credentials[key] = dump[key]
            self.user_files = dump['files']
            print("Account created successfully.")
    
    
    
    def clickLoginButton(self, user_credentials = {}):
        
        if self.primary_stacked_widget.currentWidget() == self.welcome_page_widget:
            self.initiateCommonVariables()
            self.createLoginPage()
            self.primary_stacked_widget.setCurrentWidget(self.login_page_widget)
            return
        
        error_codes = {
            '0': False, 
            '1': 'Incorrect password. Please try again.', 
            '2': 'User does not exist. Please sign up.', 
            '3': 'User is under suspension. Please contact support.'
        }
        
        dump = self.DataHandler.loginAccount(user_credentials)
        if isinstance(dump, str) and dump in error_codes:
            print(error_codes[dump])
        else:
            for key in dump:
                if key in self.user_credentials:
                    self.user_credentials[key] = dump[key]
            self.user_files = dump['files']
            print("Logged in successfully.")
    
    
    
    def clickDeleteUserButton(self):
        
        ...






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
