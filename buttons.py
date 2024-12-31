from typing import TYPE_CHECKING
from PySide6.QtWidgets import QPushButton
from variables import MEDIUM_FONT_SIZE
from PySide6.QtWidgets import QGridLayout
from utils import isEmpty, isNumorDot, isValidNumber
from variables import PRIMARY_COLOR


if TYPE_CHECKING:
    from display import Display
    from info import Info


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
    
    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)


class ButtonsGrid(QGridLayout):
    def __init__(self, display:'Display', info:'Info', *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        
        self.display = display
        self. info = info
        self._equation = ''
        self._makeGrid()
        

    @property
    def equation(self):
        return self._equation
    
    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)
        

    def _makeGrid(self):
        for rowNumber, rowData in enumerate(self._gridMask):
            for columNumber, buttonText in enumerate(rowData):
                button = Button(buttonText)
                
                if not isNumorDot(buttonText) and not isEmpty(buttonText):
                    button.setStyleSheet("""QPushButton {
                                                    color: black;
                                                    background-color: lightblue;
                                                }
                                                QPushButton:hover {
                                                    background-color: darkgray;
                                                }
                                            """)
                    
                self.addWidget(button, rowNumber, columNumber)

                buttonSlot = self._makeButtonDisplaySlot(self._insertButtronTextToDisplay, button)

                
                button.clicked.connect(buttonSlot)
    
    
    def _makeButtonDisplaySlot(self, func, *args, **kwargs):
        def realSlot():
            func(*args, **kwargs)
        return realSlot
    
    def _insertButtronTextToDisplay(self, button):
        buttonText2 = button.text()
        nweDisplayValue = self.display.text() + buttonText2
       
        if not isValidNumber(nweDisplayValue):
            return
        
        self.display.insert(buttonText2)
            
       