import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton


class HomeWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QVBoxLayout()
        self.button = QPushButton("Coucou")
        self.button.clicked.connect(self.button_clicked)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.resize(500, 500)
        self.setWindowTitle("Ma fenetre")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print("appui bouton gauche")
            print("position = " + str(event.x()) + " " + str(event.y()))

    @staticmethod
    def button_clicked():
        print("click bouton")


app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)

h_window = HomeWindow()
h_window.show()

app.exec_()
