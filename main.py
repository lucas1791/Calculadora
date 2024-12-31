import sys
from PySide6.QtGui import QIcon
from buttons import Button 
from styles import setupTheme
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit
from display import Display
from main_window import MainWindow
from variables import WINDOW_ICON_PATH
from info import Info
from buttons import ButtonsGrid




if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()
 
    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
 
    # Info
    info = Info('Sua conta')
    window.addWidgetToVlayout(info)
 
    # Display
    display = Display()
    window.addWidgetToVlayout(display)

# Grid
    buttonsGrid = ButtonsGrid(display, info)
    window.vLayout.addLayout(buttonsGrid)

    buttonsGrid._makeGrid()

 
 
    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()

    