from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs ) -> None:
        super().__init__(parent, *args, **kwargs)
        self.cw = QWidget()

        self.vLayout = QVBoxLayout()

        self.cw.setLayout(self.vLayout)

        self.setCentralWidget(self.cw)

        self.setWindowTitle('CALCULADORA')
        
    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
    
    
    def addWidgetToVlayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)
