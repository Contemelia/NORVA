class Configuration:
    
    def __init__(self, theme, accent):
        
        self.dimension = [1300, 700]
        self.stylesheet = ''
        
        self.applyPalette(theme, accent)
    
    
    
    def applyPalette(self, theme, accent):
        
        self.theme = theme if theme in ['dark', 'light'] else 'dark'
        accent = accent if accent in ['purple', 'teal'] else 'purple'
        
        available_accents = {
            'purple': self.switchAccentToPurple, 
            'teal': self.switchAccentToTeal
        }
        available_accents[accent]()
    
    
    
    def applyTheme(self):
        
        self.stylesheet = f"""
        
        QMainWindow {{
            font-family: 'Impact';
        }}
        
        
        
        QScrollArea {{
            background-color: rgba(0, 0, 0, 0);
            border-color: rgba(0, 0, 0, 0);
            border-width: 0px;
            border: none;
        }}
        
        
        
        #scrollableWidget {{
            background-color: rgba(0, 0, 0, 0);
        }}
             
        
        
        #navigationBar {{
            background-color: {self.accent['primary-item-container']};
            border-radius: 15px;
            
            color: {self.accent['primary-text']};
            font-family: 'Nirmala UI';
        }}
        
        #navigationBar:hover {{
            background-color: {self.accent['transparent-hover']};
        }}
        
        
        
        #messageBar {{
            background-color: {self.accent['message-bar']};
            border-radius: 15px;
            
            color: {self.accent['primary-text']};
            font-family: 'Nirmala UI';
        }}
        
        #messageBar:hover {{
            background-color: {self.accent['secondary-hover']};
            
            color: {self.accent['accent-text']};
        }}
        
        
        #sideBarWidget {{
            background-color: {self.accent['primary-container']};
            border-radius: 15px;
            
            color: {self.accent['primary-text']};
            font-family: 'Nirmala UI';
        }}
        
        
        
        #primaryContainer {{
            background-color: {self.accent['primary-container']};
            
            border-radius: 15px;
        }}
        
        
        #secondaryContainer {{
            background-color: {self.accent['secondary-container']};
            border-radius: 15px;
        }}
        
        
        #primaryItemContainer {{
            background-color: {self.accent['primary-item-container']};
            border-radius: 15px;
            
            color: {self.accent['primary-text']};
            font-family: 'Nirmala UI';
        }}
        
        
        #secondaryItemContainer {{
            background-color: {self.accent['secondary-item-container']};
            border-radius: 15px;
            
            color: {self.accent['primary-text']};
            font-family: 'Nirmala UI';
            padding-left: 10px;
            padding-right: 10px;
        }}
        
        #secondaryItemContainer:hover {{
            background-color: {self.accent['item-button-hover']};
        }}
        
        #secondaryItemContainer:disabled {{
            background-color: {self.accent['item-button-disabled']};
            
            color: {self.accent['disabled-text']};
        }}
        
        
        
        #primaryBoldText {{
            color: {self.accent['primary-text']};
            font-family: 'Impact';
            font-size: 10px;
        }}
        
        #primaryBoldText:hover {{
            color: {self.accent['primary-text-hover']};
        }}
        
        
        
        #primaryField {{
            background-color: {self.accent['primary-field']};
            border-radius: 10px;
            
            color: {self.accent['primary-text']};
            font-family: 'Nirmala UI';
            font-size: 10px;
            font-weight: regular;
            padding-left: 10px;
            padding-right: 10px;
        }}
        
        #primaryField:focus {{
            background-color: {self.accent['primary-field-focus']};
            
            color: {self.accent['primary-text-hover']};
            font-weight: bold;
        }}
        
        #primaryField:hover {{
            background-color: {self.accent['primary-field-hover']};
        }}
        
        #primaryField:disabled {{
            background-color: {self.accent['primary-field-disabled']};
            
            color: {self.accent['accent-text']};
        }}
        
        
        
        #itemLabel {{
            color: {self.accent['primary-text']};
            font-family: 'Nirmala UI';
            font-size: 12px;
        }}
        
        
        
        #primaryButton {{
            background-color: {self.accent['primary-button']};
            border-radius: 15px;
            
            color: {self.accent['primary-text']};
            font-size: 10px;
            font-weight: bold;
        }}
        
        #primaryButton:hover {{
            background-color: {self.accent['primary-button-hover']};
            
            color: {self.accent['primary-text-hover']};
        }}
        
        
        #itemButton {{
            background-color: {self.accent['item-button']};
            border-radius: 10px;
            
            color: {self.accent['primary-text']};
            font-size: 10px;
            font-weight: bold;
        }}
        
        #itemButton:hover {{
            background-color: {self.accent['item-button-hover']};
            
            color: {self.accent['accent-text']};
        }}
                
        
        #exitButton {{
            background-color: {self.accent['exit-button']};
            border-radius: 5px;
        }}
        
        #exitButton:hover {{
            background-color: {self.accent['hover']};
        }}
        
        
        #logoutButton {{
            background-color: {self.accent['logout-button']};
            border-radius: 5px;
        }}
        
        #logoutButton:hover {{
            background-color: {self.accent['hover']};
        }}
        
        
        
        #themeButton {{
            background-color: {self.accent['theme-button']};
            border-radius: 5px;
        }}
        
        #themeButton:hover {{
            background-color: {self.accent['hover']};
        }}
        
        
        
        #loginButton {{
            background-color: {self.accent['primary-button']};
            border-radius: 15px;
            
            color: {self.accent['primary-text']};
            font-size: 10px;
            font-weight: bold;
        }}
        
        #loginButton:hover {{
            background-color: {self.accent['primary-button-hover']};
            
            color: {self.accent['primary-text-hover']};
        }}
        
        
        
        #signUpButton {{
            background-color: {self.accent['secondary-button']};
            border-radius: 15px;
            
            color: {self.accent['secondary-text']};
            font-size: 10px;
            font-weight: bold;
        }}
        
        #signUpButton:hover {{
            background-color: {self.accent['secondary-button-hover']};
            
            color: {self.accent['secondary-text-hover']};
        }}
        
        
        
        #fileName {{
            background-color: {self.accent['primary-item-container']};
            padding-left: 10px;
            padding-right: 10px;
            border-radius: 5px;
            
            color: {self.accent['primary-text']};
            font-family: 'Nirmala UI';
            font-size: 10px;
        }}
        
        #fileName:hover {{
            background-color: {self.accent['secondary-item-container']};
        }}
        
        
        #fileExtension {{
            background-color: {self.accent['primary-item-container']};
            padding-left: 10px;
            padding-right: 10px;
            border-radius: 5px;
            
            color: {self.accent['primary-text']};
            font-family: 'Nirmala UI';
            font-size: 10px;
            font-weight: bold;
        }}
        
        #fileExtension:hover {{
            color: {self.accent['accent-text']};
        }}
        
        
        #uploadDate {{
            background-color: {self.accent['secondary-item-container']};
            padding-left: 10px;
            padding-right: 10px;
            border-radius: 5px;
            
            color: {self.accent['primary-text']};
            font-family: 'Nirmala UI';
            font-size: 10px;
        }}
        
        #uploadDate:hover {{
            background-color: {self.accent['accent-container']};
            
            color: {self.accent['secondary-text']};
        }}
        
        
        #deleteButton {{
            background-color: {self.accent['item-button-hover']};
            border-radius: 15px;
            
            color: {self.accent['exit-button']};
            font-family: 'Nirmala UI';
            font-size: 10px;
            font-weight: bold;
        }}
        
        #deleteButton:hover {{
            background-color: {self.accent['exit-button']};
            
            color: {self.accent['primary-text']};
        
        }}
        
        
        #actionButton {{
            background-color: {self.accent['item-button-hover']};
            border-radius: 15px;
            
            color: {self.accent['primary-text']};
            font-family: 'Nirmala UI';
            font-size: 10px;
            font-weight: bold;
        }}
        
        #actionButton:hover {{
            background-color: {self.accent['accent-container']};
            
            color: {self.accent['secondary-text']};
        }}
        
        """
    
    
    
    def switchAccentToPurple(self):
        
        print("Switching accent to purple")
        
        self.accent = {}    
        
        if self.theme == 'light':
            
            ...
            
        else:
            
            self.accent['background'] = '#f3e8ff'
            self.accent['primary-container'] = 'rgba(23, 23, 26, 0.7)'
            self.accent['secondary-container'] = '#07011C'
            self.accent['hover'] = '#f3e8ff'
            self.accent['alternate-hover'] = '#1d0554'
            self.accent['navigation-bar'] = '#17171A'
            self.accent['message-bar'] = 'rgba(23, 23, 26, 0.7)'
            
            self.accent['container-widget'] = 'rgba(10, 5, 20, 0.7)'
            self.accent['primary-field'] = '#09011A'
            self.accent['primary-field-hover'] = '#160F27'
            self.accent['primary-field-focus'] = '#09011A'
            
            self.accent['primary-text'] = '#f3e8ff'
            self.accent['primary-text-hover'] = '#6f00d1'
            self.accent['primary-text-hover-accent'] = '#6f00d1'
            self.accent['secondary-text'] = '#1b171f'
            self.accent['secondary-text-hover'] = '#6f00d1'
            
            self.accent['primary-button'] = '#09011A'
            self.accent['primary-button-hover'] = '#f3e8ff'
            self.accent['secondary-button'] = '#f3e8ff'
            self.accent['secondary-button-hover'] = '#09011A'
            
            
            
            self.accent['primary-container'] = 'rgba(23, 23, 26, 0.7)'
            self.accent['secondary-container'] = 'rgba(190, 179, 216, 0.1)'
            self.accent['accent-container'] = '#BEB3D8'
            self.accent['primary-item-container'] = '#17171A'
            self.accent['secondary-item-container'] = '#222126'
            self.accent['primary-hover'] = '#BEB3D8'
            self.accent['secondary-hover'] = '#17171A'
            self.accent['transparent-hover'] = 'rgba(23, 23, 26, 0.7)'
            
            self.accent['primary-text'] = '#BEB3D8'
            self.accent['secondary-text'] = '#17171A'
            self.accent['accent-text'] = '#9f0fe5'
            self.accent['disabled-text'] = '#857F73'
            
            self.accent['primary-field'] = 'rgba(190, 179, 216, 0.1)'
            self.accent['primary-field-hover'] = 'rgba(0, 0, 18, 0.7)'
            self.accent['primary-field-focus'] = 'rgba(10, 10, 30, 0.7)'
            self.accent['primary-field-disabled'] = 'rgba(190, 179, 216, 0.1)'
            
            self.accent['item-button'] = '#222126'
            self.accent['item-button-hover'] = 'rgba(190, 179, 216, 0.1)'
            self.accent['item-button-disabled'] = 'rgba(23, 23, 26, 0.3)'
            
            self.accent['theme-button'] = '#BEB3D8'
            self.accent['exit-button'] = '#E43D25'
            self.accent['logout-button'] = '#E59525'
    
        if self.theme and self.accent:
            self.applyTheme()
    
    
    
    def switchAccentToTeal(self):
        
        print("Switching accent to teal")
        
        self.accent = {}    
        
        if self.theme == 'light':
            ...
        else:
            ...
    
        if self.theme and self.accent:
            self.applyTheme()
