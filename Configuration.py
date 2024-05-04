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
            background-color: {self.accent['background']};
            
            font-family: 'Impact';
        }}
                
        
        
        #navigationBar {{
            background-color: {self.accent['navigation-bar']};
            
            border-radius: 15px;
        }}
        
        
        
        #containerWidget {{
            background-color: {self.accent['container-widget']};
            
            border-radius: 15px;
        }}
        
        
        
        #primaryField {{
            background-color: {self.accent['primary-field']};
            border-radius: 15px;
            
            color: {self.accent['primary-text']};
            font-size: 10px;
            font-weight: regular;
        }}
        
        #primaryField:focus {{
            background-color: {self.accent['primary-field-focus']};
            
            color: {self.accent['primary-text-hover']};
            font-weight: bold;
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
        
        
        
        #exitButton {{
            background-color: {self.accent['exit-button']};
            border-radius: 5px;
        }}
        
        #exitButton:hover {{
            background-color: {self.accent['hover']};
        }}
        
        
        
        #dynamicButton {{
            background-color: {self.accent['logout-button']};
            border-radius: 5px;
        }}
        
        #dynamicButton:hover {{
            background-color: {self.accent['alternate-hover']};
        }}
        
        
        
        #themeButton {{
            background-color: {self.accent['theme-button']};
            border-radius: 5px;
        }}
        
        #themeButton:hover {{
            background-color: {self.accent['alternate-hover']};
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
        
        """
    
    
    
    def switchAccentToPurple(self):
        
        print("Switching accent to purple")
        
        self.accent = {}    
        
        if self.theme == 'light':
            
            ...
            
        else:
            
            self.accent['background'] = '#f3e8ff'
            self.accent['primary-container'] = '#07011C'
            self.accent['hover'] = '#f3e8ff'
            self.accent['alternate-hover'] = '#1d0554'
            self.accent['navigation-bar'] = '#1b171f'
            
            self.accent['container-widget'] = 'rgba(10, 5, 20, 0.7)'
            self.accent['primary-field'] = '#09011A'
            self.accent['primary-field-hover'] = '#160F27'
            self.accent['primary-field-focus'] = '#09011A'
            
            self.accent['theme-button'] = '#6f00d1'
            self.accent['exit-button'] = '#f50541'
            self.accent['logout-button'] = '#dbbd25'
            
            self.accent['primary-text'] = '#f3e8ff'
            self.accent['primary-text-hover'] = '#6f00d1'
            self.accent['secondary-text'] = '#1b171f'
            self.accent['secondary-text-hover'] = '#6f00d1'
            
            self.accent['primary-button'] = '#09011A'
            self.accent['primary-button-hover'] = '#f3e8ff'
            self.accent['secondary-button'] = '#f3e8ff'
            self.accent['secondary-button-hover'] = '#09011A'
    
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