from PySide6.QtWidgets import QPushButton
from variables import MEDIUM_FONT_SIZE
from PySide6.QtWidgets import QGridLayout
from utils import isEmpty, isNumorDot
from variables import PRIMARY_COLOR
from display import Display


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
    def __init__(self, display:Display, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        
        self.display = display
        self._makeGrid()

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
        self.display.insert(buttonText2)
       